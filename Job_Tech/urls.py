from django.contrib import admin
from django.urls import path
from . import views


app_name = 'Job_Tech'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('index/register',views.regi, name='regi'),
    path('login/', views.loginPage, name="login"),
    path('', views.home, name="home"),
]

