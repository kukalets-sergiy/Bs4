import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

url = 'https://kinotron.top/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link = soup.find('div', class_='th-item').find('a', class_='th-in').get('href').split('-')[0]
ukr_name=soup.find('div', class_='th-item').find('a', class_='th-in').find('div', class_='th-title nowrap').text
year = soup.find('div', class_='th-item').find('a', class_='th-in').find(
                                                             'div', class_='th-subtitle nowrap').find('span').text[0:4]

data = []

for p in range(5):
    url = 'https://kinotron.top/films/page/{p}/'
    r = requests.get(url)
    sleep(0.5)
    soup = BeautifulSoup(r.text, 'lxml')

    films = soup.findAll('div', class_='th-item')

    for film in films:
        link = "https://kinotron.top/371" + film.find('a', class_='th-in').get('href')
        ukr_name = film.find('a', class_='th-in').find('div', class_='th-title nowrap').text
        try:
            year = soup.find('div', class_='th-item').find('a', class_='th-in').find(
                                                             'div', class_='th-subtitle nowrap').find('span').text[0:4]
        except:
            year = '-'

        data.append([link, ukr_name, year])

        print(link, ukr_name, year)

header = ['link', 'ukr_name', 'year']

df = pd.DataFrame(data, columns=header)
df.to_csv('/home/sergiy/domains/pars_uakin/kinotron_data.csv', sep=';', encoding='utf8')
