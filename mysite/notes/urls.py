from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('home/', views.home),
    path('home/view_status/', views.view_status),
    path('home/view_status/update/', views.update)
]