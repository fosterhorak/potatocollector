from django.shortcuts import render
from .models import Potato

# Create your views here.

# Add the following import
from django.http import HttpResponse
# main_app/views.py
from django.shortcuts import render


# Define the home view
def home(request):
  #return HttpResponse('<h1>Hello Potato People!</h1>')
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def potatoes_index(request):
  potatoes = Potato.objects.all()
  return render(request, 'potatoes/potatoes_index.html', {'potatoes': potatoes})

def potato_detail(request, potato_id):
  potato = Potato.objects.get(id=potato_id)
  return render(request, 'potatoes/potato_detail.html', {'potato': potato})