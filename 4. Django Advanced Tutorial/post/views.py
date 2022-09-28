from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from . import models


def list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = models.Post.objects.filter(title__icontains=q)
    else:
        posts = models.Post.objects.all()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    posts_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'posts': posts_obj})
    
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        detail = request.POST['detail']
        models.Post.objects.create(title=title, detail=detail)
        messages.success(request, 'Data has been added')
    return render(request, 'add.html')

def update(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        detail = request.POST['detail']
        post = models.Post.objects.filter(id=id).update(title=title, detail=detail)
        messages.success(request, 'Data has been updated')
    post = models.Post.objects.get(id=id)
    return render(request, 'update.html', {'post': post})

def delete(request, id):
    models.Post.objects.filter(id=id).delete()
    messages.success(request, 'Data has been deleted')
    return redirect('/post')
