from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish, Account

# Create your views here.
id = 0

def better_menu(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/better_list.html', {'dishes':dish_objects})

def add_menu(request):
    if(request.method=="POST"):
        dishname = request.POST.get('dname')
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.create(name=dishname, cook_time=cooktime, prep_time=preptime)
        return redirect('better_menu')
    else:
        return render(request, 'tapasapp/add_menu.html')

def view_detail(request, pk):
    d = get_object_or_404(Dish, pk=pk)
    return render(request, 'tapasapp/view_detail.html', {'d': d})

def delete_dish(request, pk):
    Dish.objects.filter(pk=pk).delete()
    return redirect('better_menu')

def update_dish(request, pk):
    if(request.method=="POST"):
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.filter(pk=pk).update(cook_time=cooktime, prep_time=preptime)
        return redirect('view_detail', pk=pk)
    else:
        d = get_object_or_404(Dish, pk=pk)
        return render(request, 'tapasapp/update_menu.html', {'d':d})
    
def view_login(request):
    a = ""

    if request.GET.get('page') == '1':
        a = "Account created successfully"
        
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Account.objects.filter(username=username, password=password).exists():
            return redirect('add_menu')
        else:
            a = "Invalid login"

    return render(request, 'tapasapp/login.html', {'display': a})

def view_signup(request):
    a = ""
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Account.objects.filter(username=username).exists():
            a = "Account already exists"
        else:
            Account.objects.create(username=username, password=password)
            return redirect('/?page=1')

    return render(request, 'tapasapp/signup.html', {'display': a})

def view_basic_list(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/basic_list.html', {'dishes': dish_objects})

def manage_account(request):
    return render(request, 'tapasapp/manage_account.html')

def logout(request):
    global id
    id = 0 
    
    return redirect('view_login')