from django.conf.urls import url

from . import views

app_name = 'noteay7aga'
urlpatterns = [
    url(r'^$',views.all_notes , name='all_notes'),
   # url(r'^(?P<id>\d+)$',views.note_details,name='note_details')
   url(r'^add$',views.add_notes , name='add_notes'),
   url(r'^(?P<slug>[-\w]+)/edit$',views.note_edit,name='edit_note'),
   url(r'^(?P<slug>[-\w]+)/$',views.note_details,name='note_details'),
   

   
]
