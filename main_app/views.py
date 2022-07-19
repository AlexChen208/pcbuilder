from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Case, Component
from .forms import CommentForm
# Add the following import
from django.http import HttpResponse



# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def cases_index(request):
  cases = Case.objects.all()
  return render(request, 'cases/index.html',{'cases': cases})

def cases_detail(request,case_id):
  case= Case.objects.get(id=case_id)
  id_list = case.components.all().values_list('id')
  components_case_doesnt_have = Component.objects.exclude(id__in=id_list)
  comment_form = CommentForm()
  return render(request,'cases/detail.html',{'case':case,'comment_form':comment_form, 'components': components_case_doesnt_have})

class CaseCreate(CreateView):
  model = Case
  fields = ['name', 'type', 'material', 'color', 'price']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

def add_comment(request,case_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.case_id = case_id
    new_comment.save()
  return redirect('detail', case_id=case_id)

 


class CaseUpdate(UpdateView):
  model = Case
  fields = ['name', 'type', 'material', 'color', 'price']

class CaseDelete(DeleteView):
  model = Case
  success_url = '/cases/'

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



class ComponentList(ListView):
  model = Component

class ComponentDetail(DetailView):
  model = Component

class ComponentCreate(CreateView):
  model = Component
  fields = '__all__'

class ComponentUpdate(UpdateView):
  model = Component
  fields = ['brand', 'part', 'price']

class ComponentDelete(DeleteView):
  model = Component
  success_url = '/components/'


def assoc_component(request, case_id, component_id):
  case = Case.objects.get(id=case_id)
  case.components.add(component_id)
  return redirect('detail', case_id=case_id)

def unassoc_component(request, case_id, component_id):
    case = Case.objects.get(id=case_id)
    case.components.remove(component_id)
    return redirect('detail', case_id=case_id)