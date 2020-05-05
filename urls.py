from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [

    path('author/<int:author_id>/', views.author),
    path('recipe/<int:recipe_id>', views.recipe),
    path('infoadd/', views.info_add_view),
    path('authoradd/', views.author_add_view),
    path('', views.home_index, name="homepage")
]

