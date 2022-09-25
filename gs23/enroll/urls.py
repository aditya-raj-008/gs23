from django.urls import path
from . import views

urlpatterns=[
    path('studentinfo/',views.studentinfo),
    path('studentregistration/',views.showformdata),
    path('studentapi/',views.StudentApi),
    path('studentcreateapi/',views.student_create),

] 