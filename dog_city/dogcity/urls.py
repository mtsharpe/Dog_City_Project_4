from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('owners', views.owner_list, name='owner_list'),
    path('owners/<int:pk>', views.owner_detail, name='owner_detail'),
    path('owners/new', views.owner_create, name='owner_create'),
    path('owners/<int:pk>/edit', views.owner_edit, name='owner_edit'),
    path('owners/<int:pk>/delete', views.owner_delete, name='owner_delete'),
    path('dogs', views.dog_list, name='dog_list'),
    path('dogs/<int:pk>', views.dog_detail, name='dog_detail'),
    path('dogs/new', views.dog_create, name='dog_create'),
    path('dogs/<int:pk>/edit', views.dog_edit, name='dog_edit'),
    path('dogs/<int:pk>/delete', views.dog_delete, name='dog_delete'),
    path('playdates', views.playdate_list, name='playdate_list'),
    path('playdates/<int:pk>', views.playdate_detail, name='playdate_detail'),
    path('playdates/new', views.playdate_create, name='playdate_create'),
    path('playdates/<int:pk>/edit', views.playdate_edit, name='playdate_edit'),
    path('playdates/<int:pk>/delete', views.playdate_delete, name='playdate_delete'),
    path('signup', views.signup, name='signup')
]