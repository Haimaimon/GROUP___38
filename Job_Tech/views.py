from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from tempfile import tempdir
from .models import User, Job
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm


from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User



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


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':

        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'register.html', context)