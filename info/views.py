from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from info.models import Author, Recipe
from info.forms import RecipesAddForm, AuthorAddForm, LoginForm

# Create your views here.
def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))

    form = LoginForm()

    return render(request, 'generic_form.html', {'form': form})

def home_index(req):
    recipes = Recipe.objects.all()
    return render(req, 'index.html', {
        'recipes': recipes,
    }
    )


def author(req, author_id):
    author = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author)
    return render(req, 'author.html', {
        'author': author,
        'recipes': recipes,
    }
    )


def recipe(req, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(req, 'recipe.html', {
        'recipe': recipe
    }
    )
@login_required
def recipe_add_view(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = RecipesAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                instructions=data['instructions'],
                author=data['author'],
                total_time=data['total_time'],
                description=data['description']
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = RecipesAddForm()

    return render(request, html, {'form': form})

@login_required
def author_add_view(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
           breakpoint()
           data = form.cleaned_data
           Author.objects.create(
                name=data['name'],
                bio = data['bio']
            )
           return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage'))
            )

    form = AuthorAddForm()

    return render(request, html, {'form': form})