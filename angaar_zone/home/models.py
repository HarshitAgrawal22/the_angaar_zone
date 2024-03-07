from django.db import models
from accounts.models import *

from django.contrib.auth.models import User 
# Create your models here.


class Course(models.Model):
    name=models.CharField(blank=False,null=False,max_length=30)
    description=models.TextField(blank=False,null=False)
    
    
    
    
    
class Session(models.Model):
    course=models.ForeignKey(Course,null=True,blank=True)
    teacher=models.ForeignKey(Teacher,related_name="sessions",blank=False,null=False)
    title=models.CharField(null=False,blank=False,max_length=40)
    
    time=models.DateTimeField(auto_add_now=True)
    link=models.URLField()
    
    is_Complete=models.BooleanField(null=False,default=False)
    
    notes=models.FileField(null=True,blank=True,upload_to="notes_and_files")
    
    
class Chat(models.Model):
    text=models.TextField()
    
    sender=models.ForeignKey(User,blank=False,null=False)
    receiver=models.ForeignKey(User,null=False,blank=False)
    time=models=models.DateTimeField(auto_add_now=True)
    
    