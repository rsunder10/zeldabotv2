from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify
# from bot.models import RestaurantBasic
from bot.models import Food,City,Type

# Create your models here.
def image_upload_to(instance,filename):
	print(type(instance.user.get_username()))
	basename,file_extension = filename.split(".")
	slug = slugify(basename)

	new_filename = "%s-%s.%s"%(instance.user.get_username(),slug,file_extension)
	return "avatar/%s/%s"%(instance.user.get_username(),new_filename)
def image_upload(instance,filename):

	return "zelda/%s"%(filename)

# rest =  RestaurantBasic.objects.values_list('r_type', flat=True).distinct()
class Relationship(models.Model):
	status = models.CharField(max_length =30)

	def __str__(self):
		return self.status


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	avatar = models.ImageField(upload_to = image_upload_to)
	city = models.OneToOneField(City)
	fav_food = models.ManyToManyField(Food)
	relationship = models.OneToOneField(Relationship)
	preferrs = models.ManyToManyField(Type)

	def __str__(self):
		return self.user.get_username()

class Zelda(models.Model):
	avatar = models.ImageField(upload_to = image_upload)




