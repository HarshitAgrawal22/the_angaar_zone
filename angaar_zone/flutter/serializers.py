from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from rest_framework import serializers
from accounts.models import Students,Teacher,Course
from rest_framework_simplejwt import authentication
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from icecream import ic


#=========================================================================================================================================================================================================================


class StudentRegistrationSerializers(serializers.ModelSerializer):
    password=serializers.CharField(style={
        'input_type':"password"
    },write_only=True)
    class Meta:
        model=Students
        fields=["username","password","phone_number","email"]
        extra_kwargs={
            "password":{
                "write_only":True
            }
        }
    
    def validate(self, attrs):
        #TODO add the conditions needed to validate the student 
        password=attrs.get("password")
        username=attrs.get("username")
        if password is not None and username is not None:
            return attrs
        raise serializers.ValidationError('Ivalid data sent')
    
    
    
    def create(self,validated_data):
        
        # the purpose of this method is to validate the data before registering the new Student
        student=Students.objects.create(username=validated_data.get
                                        ("username"))
        # TODO we need to add email field while registration
        student.set_password(validated_data.get("password"))
        student.save()
        return student
#=========================================================================================================================================================================================================================
   

class StudentLoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField(style={
        "input_type":"password"
    })
    class Meta: 
        model=Students
        fields=["username","password"]

#=========================================================================================================================================================================================================================

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=["id","email","username","phone_number","course"]
        
        
#=========================================================================================================================================================================================================================
       
        
        
class StudentChangePasswordSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        max_length=255,style={
            "input_type":"password"
        },write_only=True
    )
    
    class Meta:
        model=Students
        fields=["password"]
    
    
    def validate(self, attrs):
        user:Students=self.context.get("user")
        password=attrs.get("password")
        if password is not None:
            user.set_password(password)
            user.save()
            return attrs
        raise serializers.ValidationError('The password is none')
    
#=========================================================================================================================================================================================================================

class SendPasswordResetEmailStudentSerialzer(serializers.Serializer):
    username=serializers.CharField(max_length=255)
    
    class Meta:
        fields=["username"]
    
    
    def validate(self,attrs):
        username=attrs.get("username")
        # here the validate function is used to perform certain tasks like reseting password
        
        if Students.objects.filter(username=username).exists():
            
            student=Students.objects.get(username=username)
            sid=urlsafe_base64_encode(force_bytes(student.pk))
            token=PasswordResetTokenGenerator().make_token(student)
            link="https://localhost:8000/flutter//"+sid+"/"+token
            
            return attrs
        
        else: raise serializers.ValidationError('Student not registered')
        
        
#=========================================================================================================================================================================================================================

class StudentPasswordResetSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255,style={
        "input_type":"password"
    },write_only=True)
    class Meta:
        model=Students
        fields=["password"]
        
    def validate(self, attrs):
        password=attrs.get("password")
        sid=self.context.get("sid")
        token=self.context.get("token")
        ic(sid,token,password)
        try:
            if password is not None:
                id= smart_str(urlsafe_base64_decode(sid))
                student=Students.objects.get(id=id)
                
                
                if not PasswordResetTokenGenerator.check_token(student,token):
                    ic(student)
                    student.set_password(password) 
                    student.save()
                    
                    return attrs               
                else:
                    raise serializers.ValidationError('the password is none')
        except:
            raise serializers.ValidationError('token is expired or invalid')        
        