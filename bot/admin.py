from django.contrib import admin
from .models import RestaurantBasic,City,Type,Food,Menu,ContactUs
# Register your models here.

admin.site.register(RestaurantBasic)
admin.site.register(City)
admin.site.register(Type)
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(ContactUs)