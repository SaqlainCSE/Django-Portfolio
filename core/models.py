from django.db import models
import os

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    profile_image2 = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100,blank=True, null=True)
    languages = models.CharField(max_length=100,blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    experience = models.CharField(max_length=100,blank=True, null=True)
    logo = models.FileField(upload_to='skills/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    source_code = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        try:
            this = Project.objects.get(id=self.id)
            if this.image and this.image != self.image:
                # Delete the old image file if it exists and is different from new
                if os.path.isfile(this.image.path):
                    os.remove(this.image.path)
        except Project.DoesNotExist:
            # Object is new, so no old image to delete
            pass

        super().save(*args, **kwargs)

class Experience(models.Model):
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.company

class Education(models.Model):
    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.institution

class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    number = models.CharField(max_length=20, verbose_name="Contact Number", blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Sent At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

