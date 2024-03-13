from rest_framework import serializers
from accounts.models import Students,Teacher,Course
from rest_framework_simplejwt import authentication

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
        student=Students.objects.create(username=validated_data.get("username"))
        # TODO we need to add email field while registration
        student.set_password(validated_data.get("password"))
        student.save()
        return student
