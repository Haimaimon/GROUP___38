from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from tempfile import tempdir
from .models import Job, StudentJobs
from .forms import  JobForm , CreateUserForm , StudentJobForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory


def index(request):
    user = User.objects.all().values()
    context ={
        'user': user,
    }
    return render(request,'index.html',context)

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register_user(request):
    return render(request,'register.html')

def regi(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            authenticated_user = authenticate(username=username, password=password)
            login(request, authenticated_user)
            return redirect('index')
            # redirect to a success page
    else:
        form = UserRegistrationForm()
    return redirect('index')
    return render(request, 'register.html', {'form': form})

def logoutUser(request):
  logout(request)
  return redirect('login')

def index(request):
  jobs = Job.objects.all()
  context ={
        'jobs': jobs,
    }
  template = loader.get_template('index.html')
  return HttpResponse(template.render(context, request))