from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=200)
    email = forms.EmailField(label="Email Address")
    phone = forms.CharField(label="Phone Number", max_length=15)
