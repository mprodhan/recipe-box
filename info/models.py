from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=50)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField()
	favorites = models.ManyToManyField('Recipe',
                                    symmetrical=False,
                                    blank=True,
                                    related_name='favorites')

	def __str__(self):
		return self.name


	def url(self):
		return f"/author/{self.id}"

class Recipe(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	total_time = models.CharField(max_length=50)
	instructions = models.TextField(default='')
	description = models.CharField(max_length=300, default='')

	def __str__(self):
		return self.title

	def url(self):
		return f"/recipe/{self.id}"
