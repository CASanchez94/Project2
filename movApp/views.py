from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Slider, Advertisment, SocialLink, Trailer, TrailerItem, Celebrity, News, Tweet, MovieTheater, MovieTV, NewsletterSubscriber


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

def movielist(request):
    context = {
        "theater_movies": MovieTheater.objects.all(),
        "tv_movies": MovieTV.objects.all(),
        "sidebar_ad": Advertisment.objects.filter(section="sidebar").first(),
        "celebrities": Celebrity.objects.all(),
    }
    return render(request, "movielist.html", context)

def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()

        if email:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Thanks for subscribing.")
            else:
                messages.info(request, "That email is already subscribed.")
        else:
            messages.error(request, "Please enter an email address.")

    return redirect(request.META.get("HTTP_REFERER", "home"))
