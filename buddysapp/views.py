from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from buddysapp.forms import UserForm, DispensaryForm, UserFormForEdit, ProductForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from buddysapp.models import Product, Order

# Create your views here.
def home(request):
    return redirect(dispensary_home)

@login_required(login_url= '/dispensary/sign-in/')
def dispensary_home(request):
    return redirect(dispensary_orders)

# Account Info
@login_required(login_url= '/dispensary/sign-in/')
def dispensary_account(request):
    user_form = UserFormForEdit(instance=request.user)
    dispensary_form = DispensaryForm(instance=request.user.dispensary)

    if request.method == "POST":
        user_form = UserFormForEdit(request.POST, instance=request.user)
        dispensary_form = DispensaryForm(request.POST, request.FILES, instance=request.user.dispensary)

        if user_form.is_valid() and dispensary_form.is_valid():
            user_form.save()
            dispensary_form.save()

            if request.user.dispensary.logo:
                dispensary_form.fields['logo'].required = False

    return render(request, 'dispensary/account.html', {
        "user_form": user_form,
        "dispensary_form": dispensary_form})

@login_required(login_url='/dispensary/sign-in/')
def dispensary_product(request):
    product = Product.objects.filter(dispensary = request.user.dispensary).order_by("-id")
    return render(request, 'dispensary/product.html', {"product": product})

@login_required(login_url='/dispensary/sign-in/')
def dispensary_add_product(request):
    form = ProductForm()

# Once user sends data within the data, FILES updates the data. If the form is is_valid
# create it in memory then assign it to the dispensary. Products.user.Dispensary assigns the products to each dispensary
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.dispensary = request.user.dispensary
            product.save()
            return redirect(dispensary_product)

            # Passing the form to the add products page from the second line
    return render(request, 'dispensary/add-product.html', {
        "form": form
    })
@login_required(login_url='/dispensary/sign-in/')
def dispensary_edit_product(request, product_id):
    form = ProductForm(instance = Product.objects.get(id =product_id))

# Edit meal options
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance = Product.objects.get(id = product_id))

        if form.is_valid():
            form.save()
            return redirect(dispensary_product)

            # Passing the form to the add products page from the second line
    return render(request, 'dispensary/edit-product.html', {
        "form": form
    })


@login_required(login_url='/dispensary/sign-in/')
def dispensary_orders(request):
    if request.method =="POST":
        order = Order.objects.get(id = request.POST["id"], dispensary = request.user.dispensary)
        if order.status == Order.PICKING:
            order.status = Order.READY
            order.save()

    orders = Order.objects.filter(dispensary = request.user.dispensary).order_by("-id")
    return render(request, 'dispensary/orders.html', {"orders": orders})

@login_required(login_url='/dispensary/sign-in/')
def dispensary_reports(request):
    return render(request, 'dispensary/reports.html', {})

def dispensary_sign_up(request):
    user_form = UserForm()
    dispensary_form = DispensaryForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        dispensary_form = DispensaryForm(request.POST, request.FILES)

        if user_form.is_valid() and dispensary_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_dispensary = dispensary_form.save(commit=False)
            new_dispensary.user = new_user
            new_dispensary.save()

            login(request, authenticate(
            username = user_form.cleaned_data["username"],
            password = user_form.cleaned_data["password"],
            ))

            return redirect(dispensary_home)

    return render(request, 'dispensary/signup.html', {
    "user_form": user_form,
    "dispensary_form": dispensary_form
    })
