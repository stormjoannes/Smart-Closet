from Code.Bayesian import *
from Code.Functions import *
from datetime import datetime
from tkinter import *
import pytest

# def test_Weather_For_Pick_Clothes():
#     pass
    # userName = "testWeatherPick"
    # stad = "utrecht"
    # land = "nl"
    # configSignUp(userName, stad, land)
    #
    # func = "dagelijks"
    #
    # returnValue = WeatherForPickClothes(func, userName)
    # assert returnValue != None

def test_get_Time_Difference():
    firstTime = "2020-06-22"
    timeDifference = getTimeDifference(firstTime)

    assert "2" == str(timeDifference)