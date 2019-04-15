
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('counts/', views.count, name='count'),
    path('aboutus/', views.about, name='about'),
]
