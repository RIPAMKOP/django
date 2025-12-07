from django.shortcuts import render, get_object_or_404
from .models import Course


def courses_list(request):
    courses = Course.objects.all()
    return render(request, "courses_app/courses_list.html", {'courses_list': courses})


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    course.views += 1
    course.save()
    return render(request, "courses_app/course_detail.html", {'course': course})
