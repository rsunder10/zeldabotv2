from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class RestaurantBasic(models.Model):
	r_type = models.CharField(max_length = 55,blank=True)
	r_name = models.CharField(max_length = 80)
	area = models.CharField(max_length = 60,blank=True  )
	bookmark = models.IntegerField(blank=True,null=True)
	checkins = models.IntegerField(blank=True,null=True)
	city = models.CharField(max_length = 60,blank=True)
	collections = models.CharField(max_length = 100,blank=True)
	cuisines = models.CharField(max_length = 100,blank=True)
	r_address = models.CharField(max_length = 300,blank=True)
	link = models.URLField(blank=True)
	photos = models.IntegerField(null=True,blank=True)
	r_id = models.IntegerField(null = True,blank=True)
	r_latitude = models.DecimalField(max_digits = 10,decimal_places = 5,blank=True,null=True)
	r_longitude = models.DecimalField(max_digits = 10,decimal_places = 5,blank=True,null=True)
	rating = models.DecimalField(max_digits =10,decimal_places =5,blank=True,null=True)
	rating_votes = models.DecimalField(max_digits =10,decimal_places =5,blank=True,null=True)
	reviews = models.IntegerField(null=True,blank=True)
	cost = models.IntegerField(null =True,blank=True)

	def __str__(self):
		return self.r_name

class Food(models.Model):
	food_name = models.CharField(max_length = 80)
	price = models.IntegerField()

	def __str__(self):
		return self.food_name+" "+str(self.price)

class City(models.Model):
	city = models.CharField(max_length = 80)

	def __str__(self):
		return self.city

class Type(models.Model):
	types = models.CharField(max_length =80)

	def __str__(self):
		return self.types

class Menu(models.Model):
	retaurant_basic = models.OneToOneField(RestaurantBasic)
	food = models.ManyToManyField(Food)

	def __str__(self):
		return self.retaurant_basic.r_name

class ContactUs(models.Model):
	name = models.CharField(max_length=40)
	subject = models.CharField(max_length=100)
	email = models.EmailField()
	detail = models.TextField()

	def get_absolute_url(self):
		return reverse('home')

	def __str__(self):
		return self.name

