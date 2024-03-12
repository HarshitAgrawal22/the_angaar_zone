
from django.db import models
from django.contrib.auth.models import User

from imagekit.processors import ResizeToFit
from imagekit.models import ProcessedImageField


class Course(models.Model):

    name=models.CharField(blank=False,null=False,max_length=30)

    description=models.TextField(blank=False,null=False)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        
 #=========================================================================================================================================================================================================================
   
    
# Create your models here.

class Students(User):
    phone_number=models.CharField(max_length=10)
    address =models.TextField()
    parent_phone_number=models.CharField(max_length=10,null=True,blank=True)
    gender=models.CharField(choices=(
        ("female","female"),("male","male"),("Prefer not to say","Prefer not to say")
    ),max_length=30)
    course=models.ManyToManyField(Course ,blank=False,related_name="students")
    
    bio = models.TextField()
    isStudent=models.BooleanField(blank=False,null=False,default=True)
    isTeacher= models.BooleanField(default=False,blank=False ,null=False)
    
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
        


#=========================================================================================================================================================================================================================

class Teacher(User):
    phone_number=models.CharField(blank=False,null=False,max_length=10)
    bio=models.TextField(null=True,blank=True)
    
    gender=models.CharField(choices=(("Female","Female"),("Male","Male"),("Prefer not to tell","Prefer not to tell")),max_length=30)
    
    profile_pic=ProcessedImageField(upload_to="teacher_profile",
                                    processors=[ResizeToFit(width=500,height=600)],
                                    format="JPEG",options={"quality":90}
                                    )
    isTeacher= models.BooleanField(default=True,blank=False ,null=False)
    
    isStudent=models.BooleanField(blank=False,null=False,default=False)
    course=models.ForeignKey(Course,related_name="teachers",blank=False,null=False,on_delete=models.DO_NOTHING
                             
                             )
    
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
        