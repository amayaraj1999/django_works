from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
