from django.urls import path
from info import views

urlpatterns = [
    path('', views.home_index, name="homepage"),
    path('author/<int:author_id>/', views.author, name="author"),
    path('recipe/<int:recipe_id>/', views.recipe),
    path('newAuthor/', views.new_author, name="create author"),
    path('newRecipe/', views.new_recipe, name="create recipe"),
    path('newUser/', views.signup_view, name='create user'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('editrecipe/<int:recipe_id>/', views.edit_recipe, name="edit"),
    path('favorite/<int:id>/', views.favoriterecipe),
    path('unfavorite/<int:id>/', views.unfavoriterecipe),
]