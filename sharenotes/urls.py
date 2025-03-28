from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_user),
    path('register/', views.register),
    path('logout/', views.logout_user),
    path('save/', views.save_note),
    path('share/', views.share_note)
]