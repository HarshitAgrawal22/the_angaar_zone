from django.test import TestCase

# Create your tests here.
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.models import User


def get_token(user)->dict:
     # this function will give use the refresh token for teacher , student 
    refresh=RefreshToken.for_user(user)
    # this will genrate both the refresh and access token for user we are wanting
    return {
        "refresh":str(refresh),
        
        "access":str(refresh.access_token)
        
    }# got both tokens
    
    
class StudentRegistrationView(APIView):
    def get(self, request):
        serializer=StudentRegistrationSerializers(Students.objects.get(username= request.data.get("id")))
        return Response(
            {
                "User":serializer.data
            # we are getting the Student for which we are searching from User model
            }
            
        )
    
    def post(self,request):
        serializer=StudentRegistrationSerializers(data=request.data)
        
        
        
        if serializer.is_valid():
            # we have to create the isvalid method in the student registration serializer
            user=serializer.save()
            # here the user will be created 
            # new student is created and stored to the database
            
        
        
        
        
            return Response({
               "msg":"Registration Successfull",
               "data":serializer.data,
               "tokens":get_token(user)
            },status=status.HTTP_201_CREATED)
            # the stats of the user we created will be returned 
        
        
        
        
        return Response({
            "msg":serializer.errors,
        },status=status.HTTP_400_BAD_REQUEST)
        
        
        # in any other case we have simply neglected the registration and returned the errors for the request
            
# form here  i have to continue the work 

class StudentLoginView(APIView):
    
    def post(self,request):
        serializer= StudentLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            print(password,username)
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                return Response({
                    "token":get_token(user)
                },
                    status=status.HTTP_200_OK)
            else:
                return Response({
                    "error":"invalid credentials"
                },status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
