from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name='diwali_home'),
    path('wish/', views.wish, name='diwali_wish'),
]