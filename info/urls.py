from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    path('', views.home_index, name="homepage"),
    path('author/<int:author_id>/', views.author),
    path('recipe/<int:recipe_id>', views.recipe),
    path('recipeadd/', views.recipe_add_view),
    path('authoradd/', views.author_add_view),
    path('login/', views.loginview)
]
