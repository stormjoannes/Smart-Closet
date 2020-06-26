from Code.WeerAPI import *
import pytest


def test_set_values_weer():
    assert len(setValuesWeer('breda', 'nl')) == 3

def test_get_weather_details():
    assert len(getWeatherDetails('breda, nl', 'bee7d179860ed0c029ffedd7e94aea87')) == 3
