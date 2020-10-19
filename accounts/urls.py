from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import login ,logout




app_name = 'accounts'
urlpatterns = [    
    url(r'^$',views.home , name='home'),
    #path('',views.home,name='home'),
    url(r'^login/$', views.login,name='login'),    
    #path('login',views.login,name='login'),
    url(r'^logout/$', views.logout ,name='logout'),
    #path('logout',views.logout,name='logout'),
    url(r'^signup/$', views.register ,name='register') ,
    #path('signup',views.register,name='register')
    url(r'^(?P<slug>[-\w]+)/$',views.profile,name='profile'),
    url(r'^(?P<slug>[-\w]+)/edit$',views.edit_profile,name='edit_profile'),
    url(r'^(?P<slug>[-\w]+)/change_password$',views.change_password,name='change_password'),

]
