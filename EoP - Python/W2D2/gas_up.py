# review
# Refer to image given in EoP book
# Given an instance of the gasup problem, how would you efficiently compute an ample city? 
# You can assume that there exists an ample city.
# gallon[i] is the anount of gas in city i, and distance[i] is the # distance city i to the next city.

from collections import namedtuple
def find_ample_city(gallons, distance):
  remaining_gallons = 0
  CityAndRemainingGas = namedtuple('CityAndRemainingGas', ['city', 'remaining_gallons'])
  city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
  num_cities = len(gallons)
  for i in range(1, num_cities):
    remaining_gallons += gallons[i - 1] - distance[i - 1] # mpg => reupping gas at the current city we are at after traversing 
    if remaining_gallons < city_remaining_gallons_pair.remaining_gas:
      # core conditional logic is checking that we never have less gallons than what we start with at our starting city
      # this ensures that our starting city is an ample city
      # in our algo we use 0 because if we go below 0 we are out of gas
      city_remaining_gallons_pair = CityAndRemainingGas(i, remaining_gallons) 
  return city_remaining_gallons_pair.city

