from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile_view, name='profile'),
    path('skills/', views.skill_list, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education_list, name='education'),
    path('certificates/', views.certificate_list, name='certificates'),
]
