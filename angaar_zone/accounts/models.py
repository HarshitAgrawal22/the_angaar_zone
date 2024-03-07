from typing import Any
from django.db import models
from django.contrib.auth.models import User

from imagekit.processors import ResizeToFit
from imagekit.models import ProcessedImageField

from home.models import Course


# Create your models here.

class Students(User):
    phone_number=models.CharField(max_length=10)
    address =models.TextField()
    parent_phone_number=models.CharField(max_length=10,null=True,blanck=True)
    gender=models.CharField(choices=(
        ("female","female"),("male","male"),("Prefer not to say","Preer not to say")
    ))
    course=models.ManyToManyField(Course ,blank=False,related_name="students",
    on_delete=models.CASCADE)
    
    bio = models.TextField()
    isStudent=models.BooleanField(blank=False,null=False)
    
    profile_pic=ProcessedImageField(upload_to="students_profile",processors=[ResizeToFit(width=500,height=600)],format="JPEG",
                                    options={"quality":90})
    
    # models.ImageField(upload_to="student_profile",blank=True,null=True,default="student_profile/catpic.jpg")
    
    def __str__(self):
        return self.first_name
    
    
    def call(self)->dict:
        return {
            "username":self.username,
            "first_name":self.first_name,
            "last_name":self.last_name,
        }
        
    class Meta:
        verbose_name_plural = 'Students'
        
        
        verbose_name = 'Student'
        


class Teacher(User):
    phone_number=models.CharField(blank=False,null=False)
    bio=models.TextField(null=True,blank=True)
    
    gender=models.CharField(choices=(("Female","Female"),("Male","Male"),("Prefer not to tell","Prefer not to tell")))
    
    profile_pic=ProcessedImageField(upload_to="teacher_profile",
                                    processors=[ResizeToFit(width=500,height=600)],
                                    format="JPEG",options={"quality":90}
                                    )
    course=models.ForeignKey(Course,related_name="teachers",blank=False,null=False)
    
    def __str__(self):
        return self.first_name+self.last_name
    
    
    def __call__(self)-> dict:
        return {
            "username":self.username,
            "first_name":self.first_name,
            "last_name":self.last_name
            
        }
        
    class Meta:
        verbose_name_plural = 'Teachers'
        
        verbose_name = 'Teacher'
        