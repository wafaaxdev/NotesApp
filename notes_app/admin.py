from django.contrib import admin
from .models import Note
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_filter=['title','created']
    list_display=['title','created','active']
    search_fields=['title','content','slug']
    list_editable=['active']


admin.site.register(Note,NotesAdmin)

