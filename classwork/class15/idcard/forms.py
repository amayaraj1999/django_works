from django import forms
from .models import Student
from django.core.validators import FileExtensionValidator

class StudentForm(forms.ModelForm):
    id_card = forms.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )

    class Meta:
        model = Student
        fields = ['full_name', 'course', 'phone', 'email', 'id_card']
