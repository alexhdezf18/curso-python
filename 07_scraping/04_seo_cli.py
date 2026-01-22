import requests
import argparse

from bs4 import BeautifulSoup
from urllib.parse import urljoin

parser = argparse.ArgumentParser(description="Web scraping to check SEO for a given URL")
parser.add_argument('url', type=str, help='The URL of the site you want to scrape and check')
args = parser.parse_args()
url = args.url

headers = {
        'User-Agent':'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +https://www.google.com/bot.html) Safari/537.36'
    }
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('La peticion fue exitosa')

    soup = BeautifulSoup(response.text, 'html.parser')

    print(f"\033[34mRevisando la pagina: {url}\033[0m")
    print("\nSEO basico:")

    titulo_pagina = soup.title.string
    
    if titulo_pagina:
        print(f"\033[44mEl titulo de la pagina es: {titulo_pagina}\033[0m")
        if len(titulo_pagina) < 70:
            print("\033[32mEl titulo de la pagina tiene una longitud adecuada\033[0m")
        else:
            print("El titulo de la pagina es DEMASIADO largo")

    # Extrae todos los titulos h1
    titulos = [titulo.string for titulo in soup.find_all('h1')]
    if not titulos:
        print("\033[31mNo se encontraron titulos en la pagina\033[0m")
    elif len(titulos) > 1:
        print("\033[31mHay mas de un titulo h1 en la pagina033[0m")
        for titulo in titulos:
            print(titulo)
    else:
        print("\033[32mHay un titulo h1 en la pagina\033[0m")