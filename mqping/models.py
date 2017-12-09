from __future__ import unicode_literals

from django.db import models

class qmgr(models.Model):
	qmname = models.CharField(max_length=100)
	server = models.CharField(max_length=200)
	port = models.IntegerField()
	def __str__(self):
		return qmname+":"+ +server +"("+str(port)+")"
	

# Create your models here.
