from django.shortcuts import render
from .models import Slider, Advertisment, SocialLink, Trailer, TrailerItem


def index(request):
    
    context = {
        "sliders": Slider.objects.all(),
        "advertisments": Advertisment.objects.all(),
        "social_links": SocialLink.objects.all(),
        "trailers": Trailer.objects.all(),
        "trailer_items": TrailerItem.objects.all(),
        "sidebar_ad": Advertisment.objects.filter(section="sidebar").first(),
        "banner_ad": Advertisment.objects.filter(section="banner").first()
    }
    return render(request, "index.html", context)