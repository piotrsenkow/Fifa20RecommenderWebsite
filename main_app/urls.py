from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fifa-home'),
    path('about/', views.about, name='fifa-about')
]