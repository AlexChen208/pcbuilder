from django.shortcuts import render

# Add the following import
from django.http import HttpResponse


class Case:
    def __init__(self, name, color, type, material, price):
        self.name = name
        self.color = color
        self.type = type
        self.material = material
        self.price = price

cases = [
    Case('Asus', 'Black', 'Mid-Tower', 'Plastic', '$100'),
    Case('Samsung', 'White', 'Tower', 'Steel', '$200'),
    Case('Dell', 'Grey', 'Box', 'Tempered-Glass', '$250'),
   
]        

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def cases_index(request):
  return render(request, 'cases/index.html',{'cases': cases})
