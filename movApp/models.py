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
    anchor_class = models.CharField(max_length=2, blank=True)
    icon_class = models.CharField(max_length=30)
    url = models.URLField()

    def __str__(self):
        return self.name

class Trailer(models.Model):
    trailer_url = models.URLField()

    def __str__(self):
        return self.trailer_url

class TrailerItem(models.Model):
    img_src = models.ImageField(upload_to="trailers/")
    img_alt = models.CharField(max_length=100)
    img_width = models.PositiveIntegerField(default=255)
    img_height = models.PositiveIntegerField(default=170)
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=10)
    
    def __str__(self):
        return self.description

class Celebrity(models.Model):
    anchor_url = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    celebrity_url = models.CharField(max_length=200)
    celebrity_name = models.CharField(max_length=50)
    celebrity_type = models.CharField(max_length=20)

    def __str__(self):
        return self.celebrity_name

class News(models.Model):
    section = models.CharField(max_length=20)
    img_src = models.ImageField(upload_to="news/", blank=True, null=True)
    img_alt = models.CharField(max_length=100, blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)
    img_height = models.IntegerField(blank=True, null=True)

    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)  # allow empty for "more news"
    time = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Tweet(models.Model):
    content = models.CharField(max_length=280)

    def __str__(self):
        return self.content[:50]

class MovieTheater(models.Model):
    type = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.movie_title

class MovieTV(models.Model):
    type = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.movie_title

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
