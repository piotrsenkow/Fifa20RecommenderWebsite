from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fifa-home'),
    path('about/', views.about, name='fifa-about'),
    path('cam/', views.camview, name='fifa-cam'),
    path('cb/', views.cbview, name='fifa-cb'),
    path('cdm/', views.cdmview, name='fifa-cdm'),
    path('cf/', views.cfview, name='fifa-cf'),
    path('cm/', views.cmview, name='fifa-cm'),
    path('gk/', views.gkview, name='fifa-gk'),
    path('lb/', views.lbview, name='fifa-lb'),
    path('lm/', views.lmview, name='fifa-lm'),
    path('lw/', views.lwview, name='fifa-lw'),
    path('lwb/', views.lwbview, name='fifa-lwb'),
    path('rb/', views.rbview, name='fifa-rb'),
    path('rm/', views.rmview, name='fifa-rm'),
    path('rw/', views.rwview, name='fifa-rw'),
    path('rwb/', views.rwbview, name='fifa-rwb'),
    path('st/', views.stview, name='fifa-st'),
]