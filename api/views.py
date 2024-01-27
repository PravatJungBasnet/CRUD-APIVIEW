from django.shortcuts import render
from.serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['get','post','put','delete'])
def student(request,id=None):
    if request.method=='GET':
        id=request.data.get('id')
        print(request.data)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data,{'msg':'GET data'})
        else:
            print(request.data)
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            return Response(serializer.data)
    if request.method=='POST':
        stu=StudentSerializer(data=request.data)
        print(request.data)
        if stu.is_valid():
            stu.save()
            return Response(stu.data,{'msg':'Data created'},status=status.HTTP_201_CREATED)
        else:
            return Response(stu.errors)
    if request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,{'msg':'data updated'},status=status.HTTP_205_RESET_CONTENT)
        else:

            return Response(serializer.errors)
    if request.method=='DELETE':
        id=request.data.get('id')
        serializer=StudentSerializer()
        serializer.delete()