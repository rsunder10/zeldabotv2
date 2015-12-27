import sys

sys.path.append('I:\\ZELDA\\zomatobot')
                
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zomatobot.settings")
from django.conf import settings

from bot.models import RestaurantBasic
from bot.models import Area,City

rest =  RestaurantBasic.objects.values_list('city', flat=True).distinct()

for row in rest:
    k = RestaurantBasic.objects.filter(city=row).values_list('area', flat=True).distinct()
    print(row,k.count())
