from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_filter=['user','join_date','headline']
    list_display=['user','slug','headline','join_date','user_id']
    search_fields =['user__first_name','headline','bio']
    


admin.site.register(Profile,ProfileAdmin)