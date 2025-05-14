from django.shortcuts import render
from .models import Profile, Project, Skill, Experience, Education, Message
from pprint import pprint
import sys
import pprint

# Create your views here.

def dd(data):
    pprint.pprint(data)
    sys.exit()

def home(request):
    about = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    
    return render(request, 'home.html', {
        'about': about,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations
    })
    
    
def about(request):
    about = Profile.objects.first()
    skills = Skill.objects.all()
    return render(request, 'about.html', {'about': about, 'skills': skills})

def services(request):
    return render(request, 'services.html')

def experience(request):
    return render(request, 'experience.html')

def projects(request):
    return render(request, 'projects.html')

def blogs(request):
    return render(request, 'blogs.html')

def contact(request):
    return render(request, 'contact.html')


def profile_view(request):
    profile = Profile.objects.first()

    return render(request, 'profile.html', {'profile': profile})


def skill_list(request):
    skills = Skill.objects.all()

    return render(request, 'skills.html', {'skills': skills})

def experience_list(request):
    experiences = Experience.objects.all()

    return render(request, 'experience.html', {'experiences': experiences})


def education_list(request):
    education = Education.objects.all()
    
    return render(request, 'education.html', {'education': education})
