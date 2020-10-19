from django.shortcuts import render , get_object_or_404
from notes_app.models import Note
from accounts.models import Profile


# Create your views here.
def notes_home(request):
    all_notes= Note.objects.all()
    if request.user.is_authenticated:
        user = request.user
        profile = get_object_or_404(Profile,user=user)
        context={
            'all_notes':all_notes ,
            'profile':profile
        }
    else:
        context={
            'all_notes':all_notes ,
            
        }


    return render(request,'notes_home.html',context)