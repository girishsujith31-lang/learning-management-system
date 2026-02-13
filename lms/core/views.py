from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from courses.models import Note
from accounts.models import Profile

@login_required
def dashboard(request):
    # Ensure user has a profile
    profile, created = Profile.objects.get_or_create(
        user=request.user, 
        defaults={'role': 'student'}
    )
    
    context = {}
    if profile.role == 'teacher':
        context['user_notes'] = Note.objects.filter(uploaded_by=request.user)
        context['notes'] = Note.objects.all()
        return render(request, 'core/teacher_dashboard.html', context)
    else:
        context['notes'] = Note.objects.all()
        return render(request, 'core/student_dashboard.html', context)

def home(request):
    return render(request, 'core/home.html')
