from django.db import models

# Create your models here.

class ExtraInfo(models.Model):
    TYPE = {
        (0, 'Other'),
        (1, 'Horror'),
        (4, 'Drama'),
        (3, 'Sci-fi'),
        (2, 'Komedy'),
    }

    duration = models.PositiveSmallIntegerField(default=0)
    type = models.PositiveSmallIntegerField(default=0, choices=TYPE)

class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000, blank=False)
    description = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="movie_images", null=True, blank=True)
    extra = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_w_year()

    def title_w_year(self):
        return "{} ({})".format(self.title, self.year)


class Review(models.Model):
    review = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True, blank=True)

class Actor(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    films = models.ManyToManyField(Film, related_name="actors")

