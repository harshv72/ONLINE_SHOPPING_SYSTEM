from django.db import models
class User(models.Model):
	uid = models.CharField(max_length=15,primary_key=True)
	uname = models.CharField(max_length=15)
	password = models.CharField(max_length=15)
	fname = models.CharField(max_length=15)
	lname = models.CharField(max_length=15)
	dob = models.DateTimeField('date published')
	mno = models.BigIntegerField(max_length=15)
	email= models.CharField(max_length=15)
	image = models.CharField(max_length=15)
	
class Product(models.Model):
	pid = models.CharField(max_length=15,primary_key=True)
	pname = models.CharField(max_length=15)
	price = models.IntegerField(max_length=15)
	dsc = models.CharField(max_length=15)
	cid = models.CharField(max_length=15)
	category = models.CharField(max_length=15)
	image = models.CharField(max_length=15)

class Cart(models.Model):
	uid = models.CharField(max_length=15)
	pid = models.CharField(max_length=15)
	pname = models.CharField(max_length=15)
	price = models.IntegerField(max_length=15)
	qty = models.IntegerField(max_length=15)
	image = models.CharField(max_length=15)
	
class Category(models.Model):
	cid = models.CharField(max_length=15,primary_key=True)
	pid = models.CharField(max_length=15)
	pname = models.CharField(max_length=15)
 
class Buy(models.Model):
	bid = models.CharField(max_length=15,primary_key=True)
	uid = models.CharField(max_length=15)
	uname = models.CharField(max_length=15)
	pid = models.CharField(max_length=15)
	pname = models.CharField(max_length=15)
	qty = models.IntegerField(max_length=15)
	price = models.IntegerField(max_length=15)
