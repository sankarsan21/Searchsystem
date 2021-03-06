from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
