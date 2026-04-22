from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20, default="blue")

    def __str__(self):
        return self.name

class Slider(models.Model):
    image_src = models.ImageField(upload_to="slider/")
    image_width = models.PositiveIntegerField(default=285)
    image_height = models.PositiveIntegerField(default=437)
    anchor_url = models.URLField(blank=True)
    genres = models.ManyToManyField(Genre)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.movie_title
    
class Advertisment(models.Model):
    section = models.CharField(max_length=20)
    img_src = models.ImageField(upload_to="ads/")
    img_width = models.IntegerField()
    img_height = models.IntegerField()

    def __str__(self):
        return self.section

class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    anchor_class = models.CharField(max_length=2, blank="True")
    icon_class = models.CharField(max_length=30)
    url = models.URLField()

    def __str__(self):
        return self.name

class Trailer(models.Model):
    trailer_url = models.URLField()

    def __str__(self):
        return self.trailer_url
