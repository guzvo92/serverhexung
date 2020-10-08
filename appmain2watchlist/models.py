
#[MODELS / Watchlist]
from django.db import models

class Charsadminwatchlist(models.Model):
	name = models.CharField(max_length=50)

class Charfullmatrix(models.Model):
	name = models.CharField(max_length=50)
	vocation = models.CharField(max_length=50)
	levelnow = models.CharField(max_length=50)
	levelday = models.IntegerField(default='0')
	levelweek = models.IntegerField(default='0')
	levelmonth = models.IntegerField(default='0')
	lastupdate = models.CharField(max_length=50)


class Chareg(models.Model):
	name = models.CharField(max_length=50)
	vocation= models.CharField(max_length=50)
	level= models.CharField(max_length=50)
	lastlog= models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)

class CharegB1(models.Model):
	name = models.CharField(max_length=50)
	vocation= models.CharField(max_length=50)
	level= models.CharField(max_length=50)
	lastlog= models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)

class CharegB2(models.Model):
	name = models.CharField(max_length=50)
	vocation= models.CharField(max_length=50)
	level= models.CharField(max_length=50)
	lastlog= models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)

class CharegB3(models.Model):
	name = models.CharField(max_length=50)
	vocation= models.CharField(max_length=50)
	level= models.CharField(max_length=50)
	lastlog= models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)

class CharegB4(models.Model):
	name = models.CharField(max_length=50)
	vocation= models.CharField(max_length=50)
	level= models.CharField(max_length=50)
	lastlog= models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)

class CharegB5(models.Model):
	name = models.CharField(max_length=50)
	vocation= models.CharField(max_length=50)
	level= models.CharField(max_length=50)
	lastlog= models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)

class CharegB6(models.Model):
	name = models.CharField(max_length=50)
	vocation= models.CharField(max_length=50)
	level= models.CharField(max_length=50)
	lastlog= models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)

class CharegB7(models.Model):
	name = models.CharField(max_length=50)
	vocation= models.CharField(max_length=50)
	level= models.CharField(max_length=50)
	lastlog= models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)

class CharegB8(models.Model):
	name = models.CharField(max_length=50)
	vocation= models.CharField(max_length=50)
	level= models.CharField(max_length=50)
	lastlog= models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)

class CharegB9(models.Model):
	name = models.CharField(max_length=50)
	vocation= models.CharField(max_length=50)
	level= models.CharField(max_length=50)
	lastlog= models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)
