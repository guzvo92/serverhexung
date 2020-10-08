from django.db import models

class Mystery(models.Model):
	title= models.CharField(max_length=100)
	content= models.TextField()
	image = models.ImageField(default='null',upload_to ="mysteries")
	entries= models.IntegerField(default='0')
	created_at= models.DateTimeField(auto_now_add=True)

class Postmystery(models.Model):
	title= models.CharField(max_length=100)
	mystery = models.CharField(max_length=100)
	content= models.TextField()
	rate = models.IntegerField(default='0')
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)
	created_by= models.CharField(max_length=100)
