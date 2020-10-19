from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import login ,logout





app_name = 'home'
urlpatterns = [    
    url(r'^$',views.notes_home , name='notes_home'),
  
]