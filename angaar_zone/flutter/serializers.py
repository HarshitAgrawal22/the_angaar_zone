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
        
