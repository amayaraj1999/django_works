from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    id_card = models.ImageField(upload_to="id_cards/")

    def __str__(self):
        return self.full_name
