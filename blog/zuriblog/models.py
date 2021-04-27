from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()

	objects = models.Manager()

	def __str__(self):
		"""
		Returns the string representation of the Post model
		"""
		return self.title

	def get_absolute_url(self):
		return reverse('detail', args=(self.id,))
