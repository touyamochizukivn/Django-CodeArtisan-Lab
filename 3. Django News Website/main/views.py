from unicodedata import category
from django.shortcuts import render
from django.contrib import messages

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

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        models.Comment.objects.create(news=news,name=name,email=email,comment=comment)
        messages.success(request, 'Comment submitted but in moderation mode.')

    category = models.Category.objects.get(id=news.category.id)
    context = {
        'news': news,
        'related_news': category.news_set.all(),
        'comments': models.Comment.objects.filter(news=news, status=True).order_by('-id'),
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
