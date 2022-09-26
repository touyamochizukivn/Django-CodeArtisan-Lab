from unicodedata import category
from django.shortcuts import render

from . import models


def home(request):
    context = {
        'first_news': models.News.objects.first(),
        'three_news': models.News.objects.all(),
        'three_categories': models.Category.objects.all()[0:2],
    }
    return render(request, 'home.html', context)


def all_news(request):
    context = {
        'all_news': models.News.objects.all(),
    }
    return render(request, 'all-news.html', context)


def detail(request, id):
    news = models.News.objects.get(id=id)
    category = models.Category.objects.get(id=news.category.id)
    related_news = category.news_set.all()
    context = {
        'news': news,
        'related_news': related_news,
    }
    return render(request, 'detail.html', context)


def all_category(request):
    context = {
        'categories': models.Category.objects.all(),
    }
    return render(request, 'category.html', context)


def category(request, id):
    category = models.Category.objects.get(id=id)
    context = {
        'category': category,
        'all_news': category.news_set.all(),
    }
    return render(request, 'category-news.html', context)
