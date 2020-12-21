from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Potato, Accessory
from .forms import CleaningForm

# Create your views here.


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
  accessories_potato_doesnt_have = Accessory.objects.exclude(id__in = potato.accessories.all().values_list('id'))
  cleaning_form = CleaningForm()
  return render(request, 'potatoes/potato_detail.html', {
    'potato': potato, 
    'cleaning_form': cleaning_form,
    'accessories': accessories_potato_doesnt_have
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
    # can't save to the db until the potato_id is assigned
    new_cleaning = form.save(commit=False)
    # now assign the potato_id
    new_cleaning.potato_id = potato_id
    new_cleaning.save()
  return redirect('potato_detail', potato_id=potato_id)

def assoc_accessory(request, potato_id, accessory_id):
  # Note that you can pass a accessory's id instead of the whole object
  Potato.objects.get(id=potato_id).accessories.add(accessory_id)
  return redirect('potato_detail', potato_id=potato_id)

#removing an access
def de_assoc_accessory(request, potato_id, accessory_id):
  # Note that you can pass a accessory's id instead of the whole object
  Potato.objects.get(id=potato_id).accessories.remove(accessory_id)
  return redirect('potato_detail', potato_id=potato_id)


class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'description']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'