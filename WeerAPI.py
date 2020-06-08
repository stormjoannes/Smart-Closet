import requests

def setValues():
    key = 'bee7d179860ed0c029ffedd7e94aea87'
    stad = input('In welke stad staat je kledingkast: ')
    land = input('In welk Land staat je kledingkast (afkorting van land): ')
    plek = stad + ', ' + land
    return getWeatherDetails(stad, plek, key)

def getWeatherDetails(stad, plek, key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={plek}&appid={key}'
    print(url)
    print('\n')

    request = requests.get(url)

    data = request.json()

    weather = data['weather'][0]['description']
    # print(f'De weersomstandigheid in {stad} is momenteel {weather}')

    temp = data['main']['temp'] - 273.15
    # print(f'Het is momenteel {temp}°C in {stad}')

    # humidity = data['main']['humidity']
    # print(humidity)

    # windspeed = data['wind']['speed']
    # print(windspeed)
    return f'De weersomstandigheid in {stad} is momenteel {weather}' + '\n' + f'Het is momenteel {temp}°C in {stad}'
