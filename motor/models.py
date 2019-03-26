from django.db import models

# Create your models here.
class Device(models.Model):
	name = models.CharField(max_length=40)
	state = models.BooleanField(null=False, default=False)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
