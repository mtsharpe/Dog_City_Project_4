from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('dogs', views.dog_list, name='dog_list'),
    path('dogs/<int:pk>', views.dog_detail, name='dog_detail'),
    path('playdates', views.playdate_list, name='playdate_list'),
    path('playdates/<int:pk>', views.playdate_detail, name='playdate_detail')
]