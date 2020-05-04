from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [

    path('author/<int:author_id>/', views.author),
    path('', views.home_index),
    path('recipe/<int:recipe_id>', views.recipe),
]

