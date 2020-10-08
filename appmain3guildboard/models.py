from django.db import models

# Los automodels creados no tienes que llamarlos todos
# seran llamados por la condicional // NO SE PUEDE
#dado que en los modelosdb son Objetos al ser iterados db1,db2
#son transformados en texto, NECESITO UN obj("db1") asi como el str(db1)
# es es el porque del writeHG1 y createHGx1

class Allcharsguild(models.Model):
	name = models.CharField(max_length=50)

class Scopedmatrix(models.Model):
	mguildscoped = models.CharField(max_length=50)
	mcharcounter = models.IntegerField(default=0)
	created_at= models.DateTimeField(auto_now_add=True)

class Renderguildmatrix(models.Model):
	number = models.IntegerField(default='0')
	name = models.CharField(max_length=50)
	vocation = models.CharField(max_length=50)
	levelnow = models.CharField(max_length=50)
	levelday = models.IntegerField(default='0')
	levelweek = models.IntegerField(default='0')
	levelmonth = models.IntegerField(default='0')
	lastupdate = models.CharField(max_length=50)
