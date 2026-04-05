from django.shortcuts import render, redirect, get_object_or_404
from .models import Person 

id = 0

# Create your views here.
def home(request):
    person_objects = Person.objects.all()
    return render(request, 'tipsapp/home.html', {'persons':person_objects})

def pass_data(request, pk, id):
    d = get_object_or_404(Person,pk=pk)
    id = id
    return render(request, 'tipsapp/pass_data.html', {'d':d,'id':id})

def global_variable(request, pk):
    global id

    d = get_object_or_404(Person,pk=pk)
    id = d.id_number
    return render(request, 'tipsapp/pass_data.html', {'d':d,'id':id})