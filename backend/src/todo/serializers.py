from rest_framework import routers, serializers, viewsets
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = ('id', 'item','status','label')


