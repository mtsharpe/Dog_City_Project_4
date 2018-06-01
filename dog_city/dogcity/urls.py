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
    path('walks', views.walk_list, name='walk_list'),
    path('walks/<int:pk>', views.walk_detail, name='walk_detail'),
    path('walks/new', views.walk_create, name='walk_create'),
    path('walks/<int:pk>/edit', views.walk_edit, name='walk_edit'),
    path('walks/<int:pk>/delete', views.walk_delete, name='walk_delete'),
    path('signup', views.signup, name='signup')
]