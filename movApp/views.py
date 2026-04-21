from django.shortcuts import render
from .models import Slider
from django.http import HttpResponse

def index(request):
    sliders = Slider.objects.all()
    return render(request, "index.html", {
        "sliders": sliders,
    })