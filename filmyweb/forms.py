from django.forms   import ModelForm
from .models import Film, ExtraInfo, Review

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title','year', 'description', 'premiere', 'imdb_rating', 'image']

class ExtraInfoForm(ModelForm):
    class Meta:
        model = ExtraInfo
        fields = ['duration','type']



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['stars','review']

