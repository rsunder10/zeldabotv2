import sys

sys.path.append('I:\\ZELDA\\zomatobot')
                
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zomatobot.settings")
from django.conf import settings

from bot.models import RestaurantBasic
from bot.models import City

rest =  RestaurantBasic.objects.values_list('city', flat=True).distinct()
print(rest)

for row in rest:
          print(row)
          City.objects.get_or_create(city=row)
          
