from django.contrib import admin
from .models import Author, Course, Student, Teacherinfo
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name')


@admin.register(Teacherinfo)
class TeacherinfoAdmin(admin.ModelAdmin):
    list_display=('id','name')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('id','name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('id','name')








#we dont need the below line when we are using decorators
#admin.site.register(Teacher)