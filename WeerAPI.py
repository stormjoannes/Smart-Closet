import requests

def setValuesWeer(stad, land):
    key = 'bee7d179860ed0c029ffedd7e94aea87'
    plek = stad + ', ' + land
    return getWeatherDetails(stad, plek, key)

def getWeatherDetails(stad, plek, key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={plek}&appid={key}'
    print('\n')

    request = requests.get(url)

    data = request.json()

    weather = data['weather'][0]['description']

    temp = data['main']['temp'] - 273.15

    windspeed = data['wind']['speed']
    return temp, weather, windspeed
