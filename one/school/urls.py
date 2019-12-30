from django.urls import path, include
from school.views import student, single_student, staff, single_staff, index

urlpatterns = [
    path('', index, name="index"),
    path('student', student, name="student"),
    path('single_student', single_student, name="single_student"),
    path('staff', staff, name="staff"),
    path('single_staff', single_staff, name="single_staff"),
]
