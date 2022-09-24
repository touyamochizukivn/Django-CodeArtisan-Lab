from django.shortcuts import render, redirect
from django.contrib import messages

from . import models


def home(request):
    posts = models.Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
    
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
    return redirect('/')
