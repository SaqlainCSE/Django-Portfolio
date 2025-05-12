from django.contrib import admin
from .models import Profile, Skill, Project, Experience, Education, Message

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'bio', 'email', 'phone', 'address', 'profile_image', 'resume', 'created_at', 'updated_at')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'created_at', 'updated_at')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'demo_link', 'source_code', 'created_at', 'updated_at')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date', 'description', 'created_at', 'updated_at')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_year', 'end_year', 'description', 'created_at', 'updated_at')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at', 'updated_at')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Message, MessageAdmin)


