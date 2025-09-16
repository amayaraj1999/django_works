from django import forms

class MovieForm(forms.Form):
    name = forms.CharField(label="Movie Name", max_length=200)
    year = forms.IntegerField(label="Release Year")
