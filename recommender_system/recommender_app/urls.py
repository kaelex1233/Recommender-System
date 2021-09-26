from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('display-students/', views.display_students, name="display_students"),
    path('display-student-story/<str:pk>/', views.display_student_story, name="display_student_story"),
]
