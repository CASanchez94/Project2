from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Slider, Advertisment, SocialLink, Trailer, TrailerItem, Celebrity, News, Tweet, MovieTheater, MovieTV, NewsletterSubscriber


def index(request):


    sliders = Slider.objects.prefetch_related('genres').all().order_by("-id")
    sidebar_ad = Advertisment.objects.filter(section="sidebar").first()
    banner_ad = Advertisment.objects.filter(section="banner").first()
    news_list = News.objects.all()[:5]
    tweets = Tweet.objects.all()[:3]
    celebrities = Celebrity.objects.all()[:6]
    
    context = {
        "sliders": sliders,
        "social_links": SocialLink.objects.all(),
        "sidebar_ad": sidebar_ad,
        "banner_ad": banner_ad,
        "trailers": Trailer.objects.all(),
        "trailer_items": TrailerItem.objects.all(),
        "celebrities": celebrities,
        "theater_movies": MovieTheater.objects.all(),
        "tv_movies": MovieTV.objects.all(),
        "news_list": news_list,
        "tweets": tweets,

    }
    return render(request, "index.html", context)

def movielist(request):
    context = {
        "theater_movies": MovieTheater.objects.all(),
        "tv_movies": MovieTV.objects.all(),
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
