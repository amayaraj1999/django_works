from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    profile_photo = models.ImageField(upload_to='teacher_photos/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
