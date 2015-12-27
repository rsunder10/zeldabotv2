import sys

sys.path.append('I:\\ZELDA\\zomatobot')
                
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zomatobot.settings")
from django.conf import settings

from bot.models import RestaurantBasic
from bot.models import Type

rest =  RestaurantBasic.objects.values_list('r_type', flat=True).distinct()
print(rest)

for row in rest:
          print(row)
          Type.objects.get_or_create(types=row)
          
