from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from .serializer import Studentserilaiser
from .models import Student
# from rest_framework.response import Response
# from rest_framework import status




class Studentcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserilaiser
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class Studentmanage(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserilaiser
    def update(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    


        


        




# Create your views here.
