from django.shortcuts import get_object_or_404, redirect, render
from .models import Account, Supplier, WaterBottle

# Create your views here.

current_user = None

def view_supplier(request):
    global current_user
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {'suppliers': supplier_objects, 'user': current_user})


def view_bottles(request, pk):
    s = get_object_or_404(Supplier, pk=pk)
    bottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'bottles': bottle_objects, 'supplier': s})


def add_bottle(request):
    supplier_objects = Supplier.objects.all()

    if(request.method == "POST"):
        sku = request.POST.get("sku")
        brand = request.POST.get("brand")
        cost = request.POST.get("cost")
        size = request.POST.get("size")
        mouth_size = request.POST.get("mouth_size")
        color = request.POST.get("color")
        current_quantity = request.POST.get("current_quantity")
        supplier_id = request.POST.get("supplier_id")

        s = get_object_or_404(Supplier, pk=supplier_id)

        WaterBottle.objects.create(
            sku=sku,
            brand=brand,
            cost=cost,
            size=size,
            mouth_size=mouth_size,
            color=color,
            supplied_by=s,
            current_quantity=current_quantity
        )

        return redirect('view_supplier')

    else:
        suppliers = Supplier.objects.all()
        return render(request, 'MyInventoryApp/add_bottle.html', {'suppliers': suppliers})


def login_view(request):
    global current_user
    message = request.GET.get("message", "")

    if(request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")

        a = Account.objects.filter(username=username, password=password).first()

        if(a):
            current_user = a
            return redirect('view_supplier')
        else:
            message = "Invalid login"

    return render(request, 'MyInventoryApp/login.html', {'message': message})


def signup_view(request):
    if(request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")

        a = Account.objects.filter(username=username).first()

        if(a):
            return render(request, 'MyInventoryApp/signup.html', {'message': 'Account already exists'})
        else:
            Account.objects.create(username=username, password=password)
            return redirect('/?message=Account created successfully')

    return render(request, 'MyInventoryApp/signup.html')


def manage_account(request, pk):
    user_account = get_object_or_404(Account, pk=pk)
    return render(request, 'MyInventoryApp/manage_account.html', {'user': current_user})

def delete_account(request, pk):
    global current_user
    Account.objects.filter(pk=pk).delete()
    current_user = None
    return redirect('login')

def logout_view(request):
    global current_user
    current_user = None
    return redirect('login')

def change_password():
    pass