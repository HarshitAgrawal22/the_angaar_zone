
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("flutter_app/",include("flutter.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_token_pair'),path('api/token/refresh-token',TokenRefreshView.as_view(), name='token_refresh'),
    # this will be used to refresh the expired access token 
    #  the body will be like this 
     
    #  {"refresh": 
    #     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMDUyNDg5NCwiaWF0IjoxNzEwMzUyMDk0LCJqdGkiOiI4ZDE5OTkzYjBjNzk0MjJiODc5ZmM4MmU2YmJkMDNhYiIsInVzZXJfaWQiOjEwfQ.4tomm84VQXLxmEBfXrCiJJVYNhdZlajgO5UHJQaRbFE"
    # }
]
