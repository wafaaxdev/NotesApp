from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Note(models.Model):
    title   = models.CharField(max_length=50)
    content = RichTextField()
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug    = models.SlugField(blank=True, null=True) # Allow no value in Form and DB  :D
    active  = models.BooleanField(default=True)
    tags    = models.CharField(max_length=50)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    img   = models.ImageField( upload_to='notes-img',null=True,blank=True) #will create automatic on main path  :D

    # This method to assign value to slug field if it doesn't entered by value by overriding save() :D
    def save(self,*args, **kwargs):   
        if not self.slug:
            self.slug = slugify(self.title)
        super(Note,self).save(*args, **kwargs)



    def __str__(self):
        return self.title
    