from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cereal(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    brand = models.CharField(max_length = 60)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand
