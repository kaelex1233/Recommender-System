from django.db import models

# Create your models here.

class Student(models.Model):
    Employment_Status = (
    ('Employed', 'Employed'),
    ('Unemployed', 'Unemployed'),
    )

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=100, blank=True,
                            null=True, choices=Employment_Status)
    job_description = models.CharField(max_length=200, null=True)
    skills = models.CharField(max_length=200, null=True)
    date_graduated = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(
        default="default_profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Story(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
