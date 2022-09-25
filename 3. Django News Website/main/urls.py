from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('all-news', views.all_news, name='all-news'),
    path('all-category', views.home, name='all-category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
