import json

from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.models import AccessToken

from buddysapp.models import Dispensary, Product, Order, OrderDetail
from buddysapp.serializers import DispensarySerializer, ProductSerializer


def customer_get_dispensary(request):
    dispensary = DispensarySerializer(
        Dispensary.objects.all().order_by("-id"),
        many = True,
        context = {"request": request}
    ).data

    return JsonResponse({"dispensary": dispensary})

    #Linked directly to the url patters fro URLs.py. In here the urls provide the data an
    #And from here we populate that data in JSON format with the json request

    #Gets the absolute URL for the image so we pull down pictures

def customer_get_product(request, dispensary_id):
    product = ProductSerializer(
        Product.objects.filter(dispensary_id = dispensary_id).order_by("-id"),
        many = True,
        context = {"request": request}
    ).data

    return JsonResponse({"product": product})

@csrf_exempt
def customer_add_order(request):

    """
        What we need is:
        1) the get the access_token for the users to verify their account
        2) Dispensary id
        3) address of the users
        4) their order details using:
        [{"product_id": 1, "quantity": 2},{"product_id": 2, "quantity": 3}]

        return:
            {"status": "success"}
    """

    if request.method == "POST":
        # Get access_token

        access_token = AccessToken.objects.get(token = request.POST.get("access_token"),
        expires__gt = timezone.now())


        #Get Profile From Token

        customer = access_token.user.customer

        #Check whether customer  has has any orders to be DELIVERED. If the order has not been delivered the user cannot
        #place another order

        if Order.objects.filter(customer = customer).exclude(status = Order.DELIVERED):
            return JsonResponse({"status": "fail", "error": "Your last order must be completed."})


        #Check Address

        if not request.POST["address"]:
            return JsonResponse({"status": "failed", "error": "Address Is required!"})

        #Get Order Details Here

        order_details = json.load(request.POST["order_details"])

        order_total = 0
        for product in order_details:
            order_total += Product.objects.get(id = product["product_id"]).price * product["quantity"]

            if len(order_details) > 0:
                #Step 1 -Create the orders

                order = Order.objects.create(
                customer = customer,
                dispensary_id = request.POST["dispensary_id"],
                total = order_total,
                status = Order.PICKING,
                address = request.POST["address"]

                )

                #Step 2- Create Order details
                for product in order_details:
                    #checkout OrderDetails all one word
                    OrderDetail.objects.create(
                        order = order,
                        product_id = product["product_id"],
                        quantity = product["quantity"],
                        sub_total = Product.objects.get(id = product["product_id"]).price * product["quantity"]
                    )

                return JsonResponse({"status": "success"})


def customer_get_latest_order(request):
        return JsonResponse({})
