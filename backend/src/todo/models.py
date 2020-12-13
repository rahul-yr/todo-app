from django.db import models
from django.utils import timezone


STATUS_CHOICES = (
    ('pending','Pending'),
    ('done', 'Done'),
)

class Category(models.Model):
    title=models.CharField(unique=True,null=False,max_length = 100,verbose_name="Title")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")  

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

# Create your models here.
class Todo(models.Model): 
    item = models.CharField(max_length=250)
    label =models.ForeignKey(Category,null=True, blank=True, on_delete=models.SET_NULL,verbose_name="Label")
    status = models.CharField(choices=STATUS_CHOICES, max_length=10,default='pending')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        verbose_name="Todo"
        verbose_name_plural="Todo"
        ordering = ['-created_at']

    def status_as_done(self):
        self.status = 'done'
        self.updated_at = timezone.now()
        self.save()

    def status_as_pending(self):
        self.status = 'pending'
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.item