from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('student', views.student, name='student'),
    path('accounts/register', views.register, name='register')
]
