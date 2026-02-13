from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Note
from accounts.models import Profile

@login_required(login_url='accounts:login')
def upload_note(request):
    # Ensure user has a profile
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'student'}
    )
    
    if profile.role != 'teacher':
        return redirect('core:dashboard')

    if request.method == 'POST':
        Note.objects.create(
            title=request.POST['title'],
            file=request.FILES['file'],
            uploaded_by=request.user
        )
        return redirect('core:dashboard')
    return render(request, 'courses/upload_note.html')

@login_required(login_url='accounts:login')
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'courses/note_list.html', {'notes': notes})