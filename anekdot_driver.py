import requests
import re
from bs4 import BeautifulSoup

anecdot_url = 'https://anekdot-z.ru/random-anekdot'

def get_anekdot():
    webpage_response = requests.get(anecdot_url)
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, 'html.parser')
    mydivs = soup.findAll('div', class_ = 'anekdot-content')
    anekdot = re.sub(r'</span><br/><span>', '\n', str(mydivs))
    anekdot = re.sub(r'[<>[\]abcdefghijklmnopqrstuvwxyz"=/_]', '', anekdot)
    return anekdot