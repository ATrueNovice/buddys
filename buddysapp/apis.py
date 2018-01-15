from django.http import JsonResponse

from buddysapp.models import Dispensary
from buddysapp.serializers import DispensarySerializer


def customer_get_dispensary(request):
    dispensary = DispensarySerializer(
        Dispensary.objects.all().order_by("-id"),
        many = True,
        context = {"request": request}
    ).data

    return JsonResponse({"dispensary": dispensary})
