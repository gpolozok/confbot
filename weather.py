import requests
import re
from bs4 import BeautifulSoup

weather_url = 'https://www.meteoservice.ru/weather/now/moskva'

def get_weather():
    webpage_response = requests.get(weather_url)
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, 'html.parser')

    # get temperature
    mydivs = soup.findAll("div", class_="temperature")
    temperature = re.findall(r'e">(.*)<', str(mydivs))[0]

    # get weather description
    mydivs = soup.find(
        'div',
        attrs={'class':'small-12 medium-6 large-7 columns text-center'}
    )
    weather = mydivs.text

    return 'Температура за бортом: {}{}'.format(temperature, weather)