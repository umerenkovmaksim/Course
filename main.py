import requests
import PyQt5
from transliterate import translit
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def time_and_weather(city):
    ua = UserAgent()
    headers = {
        'User_Agent': ua.random
    }
    req = requests.get(f"https://pogoda.mail.ru/prognoz/{translit(city, language_code='ru', reversed=True)}", headers=headers)
    print(f"https://pogoda.mail.ru/prognoz/{translit(city, language_code='ru', reversed=True)}")
    soup = BeautifulSoup(req.text, 'lxml')
    temp_now = soup.find_all('div', class_='temp fact__temp fact__temp_size_s')

    print(temp_now)


time_and_weather('Россошь')
