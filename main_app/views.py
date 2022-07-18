from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)