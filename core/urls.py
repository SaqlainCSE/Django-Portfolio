from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('resume/', views.resume, name='resume'),
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile_view, name='profile'),
    path('skills/', views.skill_list, name='skills'),
    path('projects/', views.project_list, name='projects'),
    path('experience/', views.experience_list, name='experience'),
    path('education/', views.education_list, name='education'),
]
