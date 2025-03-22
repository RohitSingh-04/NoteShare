from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('save/', views.save_note),
    path('share/', views.share_note)
]