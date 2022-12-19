from django import forms
from .models import Job, StudentJobs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'desc', 'company']
        labels = {
            'title': 'Ttile',
            'desc': 'Desc',
            'company': 'Company',

        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'comapny': forms.TextInput(attrs={'class': 'form-control'}),

        }


class StudentJobForm(forms.ModelForm):
    class Meta:
        model = StudentJobs
        fields = ['title', 'desc', 'company', 'location']
