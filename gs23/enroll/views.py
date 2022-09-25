from django.shortcuts import render
import json
from enroll.models import Student,Teacherinfo
from enroll.forms import StudentRegistration
from django.db.models import Q
from enroll.serializer import Studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
import requests
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def studentinfo(request):
    #stu=Student.objects.filter(stuname__startswith='Aditya') | Student.objects.filter(stuname__startswith="Adil")
    #stu=Student.objects.filter(Q(stuname__startswith='Aditya') | ~Q(stuname__startswith='Aakash'))
    #stu=Student.objects.filter(pk=3).update(name="Anajli")
    qs1=Student.objects.values_list('cid','name',flat=False,named=True)
    qs2=Teacherinfo.objects.values_list('cid','name',named=True)
    stu=qs1.union(qs2)


    #r=requests.get("https://jsonplaceholder.typicode.com/users")
    #posts=r.json()
    print(stu)
    #print(stu.query)

    return render(request,'enroll/studentinfo.html',{"stu":stu})

def showformdata(request):
    fmobj=StudentRegistration(auto_id=True, label_suffix='-')
    fmobj.order_fields(['email',])
    return render(request,'enroll/userregistration.html',{'form':fmobj})
#test 1 is fine
#test 1 is not correct

#test2


def StudentApi(request):
    stud=Student.objects.all()
    serializer=Studentserializer(stud,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def student_create(request):
    if request.method =='POST':
        json_data=request.body.decode()
        print(type(json_data))
        #stream=io.BytesIO(json_data)
        #print(stream)
        stream=json.loads(json_data)
        print(stream)
        #pythondata=JSONParser().parse(stream)
        #print(pythondata)
        serializer=Studentserializer(data=stream)
        print(serializer)
        if serializer.is_valid():
            print("........................done till here.............")
            serializer.save()
            res= {'msg' : 'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
            #print("fuckyou............")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    




