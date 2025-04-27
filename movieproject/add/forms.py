from django import forms
from movie.models import Movie
from django.contrib.auth.models import User
class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','desc','trailer','banner','desc','category']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']