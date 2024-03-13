from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("register_student/",views.StudentRegistrationView.as_view(),name="register_student"),
    path("login_student/",views.StudentLoginView.as_view(),name="login_Student"),
    
    
]