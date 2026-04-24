from django.shortcuts import render
from .models import Slider, Advertisment, SocialLink, Trailer, TrailerItem, Celebrity, News, Tweet, MovieTheater, MovieTV


def index(request):
    
    context = {
        "sliders": Slider.objects.all(),
        "advertisments": Advertisment.objects.all(),
        "social_links": SocialLink.objects.all(),
        "trailers": Trailer.objects.all(),
        "trailer_items": TrailerItem.objects.all(),
        "sidebar_ad": Advertisment.objects.filter(section="sidebar").first(),
        "banner_ad": Advertisment.objects.filter(section="banner").first(),
        "celebrities": Celebrity.objects.all(),
        "theater_movies": MovieTheater.objects.all(),
        "tv_movies": MovieTV.objects.all(),
        "news_list": News.objects.all(),
        "tweets": Tweet.objects.all(),

    }
    return render(request, "index.html", context)