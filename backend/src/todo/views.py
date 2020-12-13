from django.shortcuts import render
from rest_framework import serializers
from .serializers import TodoSerializer,CategorySerializer
from . import models
from rest_framework import views, mixins, permissions, exceptions, status,viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response



class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer