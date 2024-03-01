from django.shortcuts import render, redirect
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_detail.html', {'course': course})


def rate_course(request, course_id):
    if request.method == 'POST':
        new_rating = float(request.POST['rating'])
        course = Course.objects.get(id=course_id)
        course.update_rating(new_rating)
        return redirect('course_detail', course_id=course_id)
    else:
        return render(request, 'rate_course.html', {'course_id': course_id})
