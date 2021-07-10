from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    in_print = models.BooleanField(default=True)
    def __str__(self):
        return self.title