from Code.WeerAPI import *


# class setValuesWeer(TestCase):
def test_set_values_weer():
    assert len(setValuesWeer('breda', 'nl')) == 3

# class getWeatherDetails(TestCase):
def test_get_weather_details():
    assert len(getWeatherDetails('breda, nl', 'bee7d179860ed0c029ffedd7e94aea87')) == 3