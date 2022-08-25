from email.mime import image
from turtle import width
from xml.parsers.expat import model
from django.db import models
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

def countbags(filepath):
    img=Image.open(filepath)
    height=img.height*0.026458333
    width=img.width*0.026458333
    return([height, width])

def bags(filepath):
    img=cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (11,11), 0)
    canny = cv2.Canny(blur, 30, 150, 3)
    dilated = cv2.dilate(canny, (1,1),iterations=25)
    (cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1, (0,255,0), 2)
    return len(cnt)


# Create your models here.
class Item(models.Model):
    image = models.ImageField(null=True,blank=True, upload_to="")
    width = models.IntegerField(null=True, blank =True)
    height = models.IntegerField(null=True, blank =True)
    count = models.PositiveIntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Item)
def calc(sender, instance, **kwargs):
    instance.width = countbags(instance.image.path)[1]
    instance.height = countbags(instance.image.path)[0]
    instance.count = bags(instance.image.path)
    instance.image = None
    post_save.disconnect(calc, sender=Item)
    instance.save()
    post_save.connect(calc, sender=Item)
