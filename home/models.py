from django.db import models

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=100)
	image1 = models.ImageField()
	quote1 = models.CharField(max_length=200, null=True)
	body1 = models.TextField()
	image2 = models.ImageField()
	quote2 = models.CharField(max_length=200, null=True)
	body2 = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title