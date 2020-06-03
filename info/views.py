from .forms import RecipesAddForm, AuthorAddForm, LoginForm, CreatUserForm, EditRecipeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.forms.models import model_to_dict
from info.models import Author, Recipe

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

def home_index(request, **kwargs):
    recipes = Recipe.objects.all()
    status = 'login' if not request.user.is_authenticated else 'logout'
    
    return render(request,
                  'index.html',
                   {'recipes': recipes,
                   'sign_in_button_label': status,
                   'sign_in_button_link': reverse(status)
                   })

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe.html',
                  {
                      'recipe': recipe
                  })


def author(request, author_id):
    author = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author)
    favorites = author.favorites.all()
    return render(request, 'author.html',
                  {'author': author,
                   'recipes': recipes,
                   'favorites': favorites
                  })


@login_required()
def new_author(request, **kwargs):
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            new_user = User.objects.create(
                username=data['name'],
            )
            Author.objects.create(
                name=data['name'],
                user=new_user,
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AuthorAddForm()
    return render(request, "create_author.html", {'form': form})


@login_required()
def new_recipe(request):
    html = 'create_recipe.html'

    if request.method == 'POST':
        form = RecipesAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                total_time=data['total_time'],
                description=data['description']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipesAddForm()
    return render(request, html, {'form': form})


def signup_view(request):
    html = 'newUser.html'
    form = None

    if request.method == 'POST':
        form = CreatUserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            new_user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            Author.objects.create(
                name=data['name'],
                user=new_user
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('login'))

    else:
        form = CreatUserForm()

    return render(request, html, {'form': form})


def login_view(request):
    html = 'login.html'
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )

            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    else:
        form = LoginForm()
    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def edit_recipe(request, recipe_id):
    html = 'create_recipe.html'
    rekipe = Recipe.objects.filter(id=recipe_id).first()
    if request.user.author == rekipe.author or request.user.is_staff:
        if request.method == 'POST':
            form = EditRecipeForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                title = data['title']
                time_required = data['time_required']
                description = data['description']
                instructions = data['instructions']
                rekipe.title = title
                rekipe.time_required = time_required
                rekipe.description = description
                rekipe.instructions = instructions
                rekipe.save()
                return HttpResponseRedirect(reverse('homepage'))
    else:
        return HttpResponse("frick off")
    form = EditRecipeForm(initial=model_to_dict(rekipe))
    return render(request, html,{'form': form})

@login_required()
def favoriterecipe(request, id):
    favoriterecipe = Recipe.objects.get(id=id)
    request.user.author.favorites.add(favoriterecipe)
    return HttpResponseRedirect(reverse('author', kwargs={'author_id': request.user.author.id}))

@login_required()
def unfavoriterecipe(request, id):
    favoriterecipe = Recipe.objects.get(id=id)
    request.user.author.favorites.remove(favoriterecipe)
    return HttpResponseRedirect(reverse('author', kwargs={'author_id': request.user.author.id}))
