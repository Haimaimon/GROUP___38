from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', views.admin, name="admin"),
    path('register/', views.registerPage,name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('allhr/', views.allHr, name="allhr"),
    path('<int:id>', views.view_jobs, name="view_jobs"),
    path('add/', views.add, name= "add"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('profile/', views.my_profile, name="profile"),
    path('studentjob/', views.studentjobs, name="studentjob"),
    path('jobseeker/', views.userPage, name='jobseeker'),
    path('portfolio/', views.portFolio, name="portfolio"),
    path('user/', views.userr, name="user"),
    path('upload/', views.upload_file, name="upload"),
    path('profileseeker/',views.profileseeker, name="profileseeker"),
    path('searchjob/',views.search_job, name="searchjob"),
    path('delete/', views.deleteProfile, name="delete"),
    path('job_submission/', views.submission, name="job_submission"),
    path('portfolio_hr/', views.portFolio_hr, name="portfolio_hr"),

    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_send.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
]

