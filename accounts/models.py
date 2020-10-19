from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #first_name= models.CharField(max_length=50)   we remove form profile model because Django provide them automatically
    #last_name= models.CharField( max_length=50)
    headline =models.CharField(max_length=50)
    bio=models.TextField()
    slug = models.SlugField(blank=True, null=True)
    img=models.ImageField(upload_to="profile_img")
    join_date= models.DateField( auto_now=False, auto_now_add=False,default=datetime.datetime.now())


    def save(self,*args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.user)
        super(Profile,self).save(*args, **kwargs)

    def __str__(self):
        #return self.user 
        return '%s' %(self.user)
    
## Signals ## Automatically create profile once user_account created :D

def create_profile(sender , **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile ,sender=User)