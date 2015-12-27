import sys


sys.path.append('I:\\ZELDA\\zomatobot')
                
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zomatobot.settings")
from django.conf import settings

from bot.models import RestaurantBasic

import csv

reader = csv.reader(open("I:\\ZELDA\\zomatobot\\restaurants.csv"), dialect='excel')

for row in reader:
      if row[0] != 'r_type': # Ignore the header row, import everything else
          print('hi')
          
          print(row[0])
          r_types = row[0]
          r_names = row[1]
          areas = row[2]
          bookmarks = row[3]
          if bookmarks =='':
              bookmarks=0
          checkinss = row[4]
          if checkinss=='':
              checkinss=0
          citys = row[5]
          collectionss = row[6]
          cost =row[7]
          if cost =='':
              cost=0
          cuisiness = row[8]
          r_addresss = row[9]
          links = row[10]
          photoss = row[11]
          if photoss == '':
              photoss=0
          r_ids = row[12]
          if r_ids =='':
              r_ids=0
          r_latitudes = row[13]
          if r_latitudes =='':
              r_latitudes=0
          r_longitudes = row[14]
          if r_longitudes== '':
              r_longitudes=0
          ratings = row[15]
          if ratings=='':
              ratings=0
          rating_votess = row[16]
          if rating_votess =='':
              rating_votess=0
          reviewss = row[17]
          if reviewss=='':
              reviewss=0

          RestaurantBasic.objects.get_or_create(r_type=r_types,r_name=r_names,area=areas,bookmark=bookmarks,checkins=checkinss,city=citys,collections=collectionss,cuisines=cuisiness,r_address=r_addresss,link=links,photos=photoss,r_id=r_ids,r_latitude=r_latitudes,r_longitude=r_longitudes,rating=ratings,rating_votes=rating_votess,reviews=reviewss,cost=cost)
          
