from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_index, name="homepage"),
    path('author/<int:author_id>/', views.author),
    path('recipe/<int:recipe_id>', views.recipe),
    path('recipeadd/', views.recipe_add_view),
    path('authoradd/', views.author_add_view),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('editrecipe/<int:recipe_id>', views.edit_recipe, name="edit"),
    path('favorite/<int:id>/', views.favoriterecipe),
    path('unfavorite/<int:id>/', views.unfavoriterecipe),
]
