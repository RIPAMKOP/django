from django.shortcuts import render
from .models import course



def courses_list(request):
    courses = course.objects.all()
    
    return render(request, "courses_app/courses_list.html", context={'courses_list' : courses})