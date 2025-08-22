from django.db import models

# Create your models here.
class Create_Post(models.Model):
    title=models.CharField(max_length=100,null=True)
    content=models.TextField(max_length=100,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
