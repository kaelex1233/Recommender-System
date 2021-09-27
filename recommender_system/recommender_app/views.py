from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .filters import StudentInfoFilter
# Create your views here.

def display_students(request):
    students = Student.objects.all()

    filter = StudentInfoFilter(request.GET, queryset=students)
    students = filter.qs

    context = {'students': students, 'filter': filter}
    return render(request, 'recommender_app/students.html', context)

def display_student_story(request, pk):
    student = Student.objects.get(id=pk)
    story = student.story_set.all()

    context = {'student': student,'story': story}
    return render(request, 'recommender_app/display_student_story.html', context)
