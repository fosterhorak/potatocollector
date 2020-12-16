from django.shortcuts import render

# Create your views here.

# Add the following import
from django.http import HttpResponse
# main_app/views.py
from django.shortcuts import render

# adding Potato class & list (temporary until database added)
class Potato:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, birth_place, length, weight, age, description):
    self.name = name
    self.birth_place = birth_place
    self.length = length
    self.weight = weight
    self.age = age
    self.description = description

potatoes = [
  Potato('Bert', 'Idaho', '5 inches', '4 ounces', 3, 'lively fellow'),
  Potato('Spud', 'Kansas', '8 inches', '8 ounces', 5, 'a rotund tater'),
  Potato('Idaho', 'Oklahoma', '4 inches', '3 ounces', 2, 'shy little guy'),
  Potato('Mashed', 'Montana', '6 inches', '7 ounces', 14, "he's seen better days"),

]




# Define the home view
def home(request):
  #return HttpResponse('<h1>Hello Potato People!</h1>')
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def potatoes_index(request):
  return render(request, 'potatoes/potatoes_index.html', {'potatoes': potatoes})

