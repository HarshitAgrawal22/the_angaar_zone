
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from schema_graph.views import Schema
urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path("flutter_app/",include("flutter.urls")),
    
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_token_pair'),
    
    
    path('api/token/refresh-token',TokenRefreshView.as_view(), name='token_refresh'), # this will be used to refresh the expired access token 
    #  the body will be like this 
    
    
    path("schema/",Schema.as_view()),
    # this will help us to get the schema of the database models
    
    
    
    path(r"^schema/$",Schema.as_view()),
   
     
  
]
