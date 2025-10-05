from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'subject', 'years_of_experience', 'profile_photo']

    def clean_profile_photo(self):
        photo = self.cleaned_data.get('profile_photo')
        if photo:
            ext = photo.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError("Only .jpg, .jpeg, .png files are allowed.")
        return photo
