from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name='chhath_home'),
    path('wish/', views.wish, name='chhath_wish'),
]