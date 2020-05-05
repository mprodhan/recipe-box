from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=50)
	bio = models.TextField()
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