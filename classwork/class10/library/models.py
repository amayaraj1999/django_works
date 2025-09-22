from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    year = models.CharField(max_length=500)

    def __str__(self):
        return self.title    