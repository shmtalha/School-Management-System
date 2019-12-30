from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {

    }
    return render(request, "index.html", context)


def student(request):
    context = {

    }
    return render(request, "students.html", context)


def single_student(request):
    context = {

    }
    return render(request, "single_student.html", context)


def staff(request):
    context = {

    }
    return render(request, "staff.html", context)


def single_staff(request):
    context = {

    }
    return render(request, "single_staff.html", context)
