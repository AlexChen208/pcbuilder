from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Case, Component, Photo
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
import os

# Add the following import
from django.http import HttpResponse
import os


# Define the home view

def home(request):
  cases= Case.objects.all()
  return render(request,'home.html',{'cases':cases})

def about(request):
  return render(request, 'about.html')

@login_required
def cases_index(request):
  cases = Case.objects.filter(user=request.user)
  return render(request, 'cases/index.html',{'cases': cases})


def cases_detail(request,case_id):
  case= Case.objects.get(id=case_id)
  id_list = case.components.all().values_list('id')
  components_case_doesnt_have = Component.objects.exclude(id__in=id_list)
  comment_form = CommentForm(request.POST)
  return render(request,'cases/detail.html',{'case':case,'comment_form':comment_form, 'components': components_case_doesnt_have})

class CaseCreate(LoginRequiredMixin,CreateView):
  model = Case
  fields = ['name', 'type', 'material', 'color', 'price']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

@login_required
def add_comment(request,case_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.case_id = case_id
    new_comment.name = request.user
    new_comment.save()
  return redirect('detail', case_id=case_id)

def some_function(request):
  secret_key = os.environ['SECRET_KEY']


class CaseUpdate(LoginRequiredMixin,UpdateView):
  model = Case
  fields = ['name', 'type', 'material', 'color', 'price']

class CaseDelete(LoginRequiredMixin,DeleteView):
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



class ComponentList(LoginRequiredMixin,ListView):
  model = Component

class ComponentDetail(LoginRequiredMixin,DetailView):
  model = Component

class ComponentCreate(LoginRequiredMixin,CreateView):
  model = Component
  fields = '__all__'

class ComponentUpdate(LoginRequiredMixin,UpdateView):
  model = Component
  fields = '__all__'

class ComponentDelete(LoginRequiredMixin,DeleteView):
  model = Component
  success_url = '/components/'

@login_required
def assoc_component(request, case_id, component_id):
  case = Case.objects.get(id=case_id)
  case.components.add(component_id)
  return redirect('detail', case_id=case_id)

@login_required
def unassoc_component(request, case_id, component_id):
    case = Case.objects.get(id=case_id)
    case.components.remove(component_id)
    return redirect('detail', case_id=case_id)

@login_required
def add_photo(request, case_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, case_id=case_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
  return redirect('detail', case_id=case_id)