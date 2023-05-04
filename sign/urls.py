from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SignView.as_view()),
    path('project/', views.project),
]