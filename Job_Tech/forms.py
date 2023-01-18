from django import forms
from.models import StudentJobs , AllJob , Hr , JobSeeker,FileModel
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    STATUS_CHOICES = [
        ('hr', 'Hr'),
        ('job_seeker', 'Job_seeker'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','status']    

class HrForm(forms.ModelForm):
    class Meta:
        model = Hr
        fields = '__all__'
        exclude = ['user']

class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = '__all__'
        exclude = ['user']
        
class AllJobsForm(forms.ModelForm):
     AGE_CHOICES = [
         ('18-24','18-24'),
         ('25-35','25-35'),
         ('35+','35+'),
     ]
     age = forms.ChoiceField(choices=AGE_CHOICES,required=True)
     class Meta:
        model = AllJob
        fields = '__all__'
    
class StudentJobForm(forms.ModelForm):
    class Meta:
        model = StudentJobs
        fields = ['title','desc','company','location']
        labels = {
            'title': 'Ttile',
            'desc': 'Desc',
            'company':'Company',
            'location':'Location'
            
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),
            'comapny': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
        }
               

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = '__all__'            