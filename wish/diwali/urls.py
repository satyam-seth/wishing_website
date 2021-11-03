from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='diwali_home'),
]