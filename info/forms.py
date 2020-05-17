from django import forms
from info.models import Author

class RecipesAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    total_time = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)

class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    
class CreatUserForm(forms.Form):
    name = forms.CharField(max_length=90)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class EditRecipeForm(forms.Form):
    title = forms.CharField(max_length=20)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time_required = forms.CharField(max_length=90)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
