from django.contrib import admin
from . import models
# from .

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Todo)