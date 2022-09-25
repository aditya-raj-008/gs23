from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

    #comment=models.CharField(max_length=40, default="not available")

#we are using model admin class instead
    #def __str__(self):
        #return str(self.stuid)
class Teacherinfo(models.Model):
    #stuid=models.IntegerField(primary_key=True)
    cid=models.IntegerField()
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    
class Student(models.Model):
    #stuid=models.IntegerField(primary_key=True)
    cid=models.IntegerField()
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=70)
    teacher_info=models.ForeignKey(Teacherinfo,on_delete=models.CASCADE,blank=True,null=True)

    #def __str__(self):
        #return self.name

class Author(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=30)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="courses")

    def __str__(self):
        return self.name
