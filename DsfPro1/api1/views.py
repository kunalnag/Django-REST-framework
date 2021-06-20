import django
from rest_framework import serializers
from django.shortcuts import render
from .models import Student
from .serializiers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

import io
from rest_framework.parsers import JSONParser 
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Single Model object.



def student_detail(request,pk):
    
    #Student model object
    stu = Student.objects.get(id=pk) 
    #Serializers convert student model object to python dictionary
    serializers = StudentSerializer(stu)
    #JSONRenderer convert student python dictionary to json object
    # json_data = JSONRenderer().render(serializers.data)

    # return HttpResponse(json_data,content_type='application/json')

    #use simply to reduce the extra line of code
    return JsonResponse(serializers.data)

def student_list(request):

    #Student model object
    stu = Student.objects.all()
    #Serializers convert student model object to python dictionary
    serializers = StudentSerializer(stu,many=True)
    #JSONRenderer convert student python dictionary to json object
    # json_data = JSONRenderer().render(serializers.data)

    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializers.data,safe=False)

@csrf_exempt
def create(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data inserted','code':200}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data)
        