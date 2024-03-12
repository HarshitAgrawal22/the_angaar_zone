from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display=["id","course","teacher","title","time","start_time" ]
    search_fields=["course","id","title"]
    list_filter=["course","teacher"]




#==================================================================================================================================================




@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display=["sender","receiver","text","creation_time"]
    search_fields=["sender","receiver"]
    list_filter=["sender","receiver"]




#==================================================================================================================================================




@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display=["course","created_at","is_Submitted","title",]
    search_fields=["title","course"]
    list_filter=["course"]




#==================================================================================================================================================




@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display=["assignment","student","answer"]
    search_fields=["assignment"]
    list_filter=["student","assignment"]




#==================================================================================================================================================




@admin.register(EligibleForCertificate)
class EligibleForCertificateAdmin(admin.ModelAdmin):
    list_display=["student","course"]
    search_fields=["student"]
    list_filter=["student","course"]




#==================================================================================================================================================





