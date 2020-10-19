from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from .models import Profile
from django.shortcuts import get_object_or_404
from .froms import UserForm , ProfileForm
from django.contrib import messages



# Create your views here.
#star Home
def home(request):
    pass
#end Home


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username ,password= password)

        if user is not None:
            auth.login(request,user)
            return redirect('/notes')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('/accounts/login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):

    if request.method == 'POST': 
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username is taken ..')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email is taken')
                    return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name = first_name ,last_name = last_name ,email = email ,password = password1)
                user.save()
                return redirect('/accounts/login')
        else:
            messages.info(request,'Password is not matched')
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'register.html')

def profile(request,slug):
    profile = get_object_or_404(Profile,slug=slug) #Profile.objects.get(slug=slug)   

    context = {
        'profile':profile
    }
    return render(request,'profile.html',context)

def edit_profile(request , slug):
    profile = get_object_or_404(Profile,slug=slug) #3shan edit 7aga lazm tgeeblo el7aga nfsaha el awl :D 
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user) 
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user =user_form.save()

            profile =profile_form.save(commit=False)
            profile.user = user
            if 'img' in request.FILES:
                profile.img = request.FILES['img']
                profile.save()
                messages.success(request, 'Profile has been updated successfully.')
                return redirect('/dit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    
    
    user = request.user
    profile = get_object_or_404(Profile,user=user)
    context ={
        'user_form':user_form,
        'profile_form':profile_form,
        'profile':profile
    }

    return render(request,'edit_profile.html',context)

def change_password(request,slug):
    if request.user.is_authenticated:
        profile = get_object_or_404 (Profile,slug=slug)
        user = request.user
        profile = get_object_or_404(Profile,user=user)

    

        if request.method == 'POST':
            password_form = PasswordChangeForm(request.user,request.POST)

            if password_form.is_valid():
                password_form.save()
                return redirect('/')


        else:
            password_form = PasswordChangeForm(request.user)
    else:
         return redirect('/accounts/login') 
    
    context={
        'password_form':password_form,
        'profile':profile
    }
    return render(request,'change_password.html',context)