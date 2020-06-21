# from unittest import TestCase
import pytest
from WeerAPI import *

# class setValuesWeer(TestCase):
def test_set_values_weer():
    assert len(setValuesWeer('breda', 'nl')) == 3



# # class getWeatherDetails(TestCase):
# def test_get_weather_details(self):
#     self.object = getWeatherDetails(plek="breda, nl", key='bee7d179860ed0c029ffedd7e94aea87')
#     print(self.object)
#     self.assertEquals(3, len(self.object))

test_set_values_weer()
