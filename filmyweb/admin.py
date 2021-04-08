from django.contrib import admin
from .models import Film, ExtraInfo, Review, Actor

# Register your models here.

#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ["title"]
    #exclude = ['year']
    list_display = ['title', 'imdb_rating']
    list_filter = ["year"]
    search_fields = ('title','description')

admin.site.register(ExtraInfo)
admin.site.register(Review)
admin.site.register(Actor)
