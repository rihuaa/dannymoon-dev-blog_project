from django.db import models


# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User') # Depends on the User
	title = models.CharField(max_length=100) # Title
	text = models.TextField();
	created_date = models.DateTimeField(auto_now_add=True) # Date for time creation
	picture = models.FileField(default=None, blank=True)

	def __str__(self):
		return self.title