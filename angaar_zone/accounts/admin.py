from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header="Angaar Batch"

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display=["id","username","first_name","last_name","phone_number","gender","parent_phone_number","last_login"]
    exclude=[
        "email","is_superuser","date_joined","groups","user_permissions"
    ]
    search_fields=["username","phone_number","first_name","id"]
    list_filter=["course","gender"]
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=["username","first_name","last_name","phone_number","last_login"]
    exclude=["password","email","is_active","is_superuser","date_joined","groups","user_permissions"]
    search_fields=["username","first_name","last_name"]
    list_filter=["course"]




@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=["id","name","description"]
    search_fields=["id","name"]


