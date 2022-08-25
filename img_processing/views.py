from tkinter import Image
from django.http import JsonResponse
from django.shortcuts import render
from .models import Item
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ImageSerializer
from img_processing import serializers


# Create your views here.
def model(image):
    return 10

# def count_retrieval(request):
#     serializer_class = ImageSerializer  



class ImageViewSet(viewsets.ModelViewSet):
    try:
        serializer_class = ImageSerializer 
        serializer_class.count = model(serializer_class.image)   
        queryset = Item.objects.all()
    except Exception as e:
        print(e)  
    # def create(self, request):
    #     obj = self.get_object()
    #     count=model(obj.image)
    #     obj.count = count
    #     obj.save()
    #     print(obj)
    #     return Response({'status': 'success'})


def view(request):
    item = Item.objects.all()
    context={"item":item}
    return render(request,'img_processing/count.html',context)
