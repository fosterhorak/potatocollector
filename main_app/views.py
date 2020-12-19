from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Potato
from .forms import CleaningForm

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
  cleaning_form = CleaningForm()
  return render(request, 'potatoes/potato_detail.html', {
    'potato': potato, 
    'cleaning_form': cleaning_form
  })

class PotatoCreate(CreateView):
  model = Potato
  fields = '__all__'

class PotatoUpdate(UpdateView):
  model = Potato
  fields = ['birth_place', 'length', 'weight', 'age', 'description']

class PotatoDelete(DeleteView):
  model = Potato
  success_url = '/potatoes/'

def add_cleaning(request, potato_id):
  # create a model form instance using the data in request.POST
  form = CleaningForm(request.POST)
  # validate that the form is good
  if form.is_valid():
    # can't save to the db until the cat_id is assigned
    new_cleaning = form.save(commit=False)
    # now assign the cat_id
    new_cleaning.potato_id = potato_id
    new_cleaning.save()
  return redirect('potato_detail', potato_id=potato_id)

 