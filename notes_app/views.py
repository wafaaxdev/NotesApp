from django.shortcuts import render ,redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Note
from .forms import NoteForm
from django.contrib import messages
from accounts.models import Profile


# Create your views here.

def all_notes(request):
    if request.user.is_authenticated:            
        user = request.user
        profile = get_object_or_404(Profile,user=user)
        all_notes = Note.objects.filter(user=user)
        context = {
            'all_notes': all_notes,
            'profile':profile
        }
        return render(request,'notes.html',context)
    else:
        return redirect('/accounts/login')

def note_details(request,slug):
    note = Note.objects.get(slug=slug)
    if request.user.is_authenticated:
        user = request.user
        profile = get_object_or_404(Profile,user=user)
        context={
            'note':note,
            'profile':profile
        }
        
        return render(request,'one_note.html',context)
    else:
        context={
            'note':note,
            
        }
        
        return render(request,'one_note.html',context)

def add_notes(request):
    if request.user.is_authenticated:
        user = request.user
        profile = get_object_or_404(Profile,user=user)
        if request.method == 'POST':
            form = NoteForm(request.POST,request.FILES) # constructor

            if form.is_valid():
                new_form = form.save(commit=False)  # class instance or object
                new_form.user = request.user
                new_form.save()
                messages.success(request,'Note has been created successfully.')            
                return redirect('/notes')
        else:
            form = NoteForm()     

    else:
        return redirect('/accounts/login')

    context = {
        'form':form,
        'profile':profile
    }

    return render(request,'add_note.html',context)
    
def note_edit(request,slug):
    if request.user.is_authenticated:
        user = request.user
        profile = get_object_or_404(Profile,user=user)
        note = Note.objects.get(slug=slug)
        if request.method == 'POST':     #means you clicked the button  :D
            form = NoteForm(request.POST,request.FILES,instance=note)
            
            if form.is_valid():
                new_form = form.save(commit=False)  # class instance or object
                new_form.user = request.user
                new_form.save()
                messages.success(request, 'Note has been updated successfully.') 
                return redirect('/notes')
        else:
            form = NoteForm(instance=note)     

        context = {
            'form':form,
            'profile':profile
        }

        return render(request,'edit_note.html',context)
    else:
        return redirect('/accounts/login')
