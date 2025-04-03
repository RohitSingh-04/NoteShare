from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "new"),
    path('login/', views.login_user),
    path('register/', views.register),
    path('logout/', views.logout_user, name = "logout"),
    path('save/', views.save_note),
    path('share/<int:note_id>', views.share_note),
    path('show-notes/', views.show_notes),
    path('open/<int:note_id>/', views.open_note, name = 'open_note'),
    path('update/<int:note_id>/', views.update_note),
    path('profile/', views.profile),
]