from django.shortcuts import render

from . import models


def home(request):
    context = {
        'first_news': models.News.objects.first(),
        'three_news': models.News.objects.all()[1:3],
        'three_categories': models.Category.objects.all()[0:2],
    }
    return render(request, 'home.html', context)


def all_news(request):
    context = {
        'all_news': models.News.objects.all(),
    }
    return render(request, 'all-news.html', context)