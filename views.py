from django.shortcuts import render, reverse, HttpResponseRedirect
from django.shortcuts import render

from info.models import Author, Recipe
from info.forms import RecipesAddForm, AuthorAddForm

# Create your views here.
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

def author_add_view(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio = data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()

    return render(request, html, {'form': form})