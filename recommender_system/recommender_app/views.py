from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
# Create your views here.

def display_students(request):
    student = Student.objects.all()

    context = {'student': student}
    return render(request, 'recommender_app/display_students.html', context)

def display_student_story(request, pk):
    student = Student.objects.get(id=pk)
    story = student.story_set.all()

    context = {'student': student,'story': story}
    return render(request, 'recommender_app/display_student_story.html', context)