from django.db import models
from accounts.models import Students,Teacher,Course
from django.utils import timezone
from django.contrib.auth.models import User 
# Create your models here.



#=========================================================================================================================================================================================================================
    
class Session(models.Model):
    
    course=models.ForeignKey(Course,null=True,blank=True,on_delete=models.CASCADE)
    
    teacher=models.ForeignKey(Teacher,related_name="sessions",blank=False,null=False,
                              on_delete=models.PROTECT
                              
                              )
    
    title=models.CharField(null=False,blank=False,max_length=40)
    
    
    time=models.DateTimeField(auto_now_add=True)
    
    link=models.URLField()
    start_time=models.DateTimeField()
    
    is_Complete=models.BooleanField(null=False,default=False)
    
    
    notes=models.FileField(null=True,blank=True,upload_to="notes_and_files")
    
    def __str__(self) -> str:
        return self.title 
    
    def get_course_name(self)->str:
        return self.course
    
    def get_meeting_status(self):
        now = timezone.now()
        if self.start_time > now:
            return {
                "color": "danger",
                "status": "Upcoming"
            }

        elif self.is_completed == True:
            return {
                "color": "success",
                "status": "Finished"
            }

        elif self.start_time < now:
            return {
                "color": "info",
                "status": "Ongoing"
            }

        else:
            return {
                "color": "danger",
                "status": "Error"
            }
        
    

#=========================================================================================================================================================================================================================
    
class Chat(models.Model):
    text=models.TextField()
    
    sender=models.ForeignKey(User,blank=False,null=False,related_name="chats",
    on_delete=models.CASCADE)
    
    receiver=models.ForeignKey(User,null=False,blank=False,related_name="chat",
    on_delete=models.CASCADE)
    
    creation_time=models.DateTimeField(auto_now_add=True)
    

#=========================================================================================================================================================================================================================
class Assignment(models.Model):
    
    course=models.ForeignKey(Course,related_name="assignment",
                             blank=False,null=False,max_length=30,
                             on_delete=models.CASCADE)
    
    created_at=models.DateField(auto_now_add=True)
    
    is_Submitted=models.BooleanField(default=False)
    
    title=models.CharField(max_length=30)
    
    due_date=models.DateField()
    
    url=models.URLField()
    
    def __str__(self) -> str:
        return self.title
    def is_Completed(self)->bool:    
        return timezone.now().date()>self.due_date


#=========================================================================================================================================================================================================================

class Submission(models.Model):
    
    assignment=models.ForeignKey(Assignment,related_name="submission",on_delete=models.CASCADE) 
    
    
    student=models.ForeignKey(
        Students,on_delete=models.CASCADE)
    
    answer=models.TextField(blank=True,null=True)
    
    file=models.FileField(blank=True,null=True)
    
    submitted_at= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"Submission by {self.student.first_name} for {self.assignment.title}  => {self.answer}"
    



#=========================================================================================================================================================================================================================

class EligibleForCertificate(models.Model):
    student=models.ForeignKey(Students,on_delete=models.CASCADE)
    
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.student.username} is eligible for {self.course.name}"