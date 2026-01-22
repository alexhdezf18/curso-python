import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://es.wikipedia.org/wiki/Web_scraping'

def scrape_url(url: str):
    headers = {
        'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +https://www.google.com/bot.html)'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print('La peticion fue exitosa')

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraer todos los titulos <h1>
        titulos = [titulo.string for titulo in soup.find_all('h1')]
        print(titulos)

        # Extraer todos los enlaces <a>
        # Con el urljoin podemos tranformar todos los enlaces en su formato completo
        enlaces = [urljoin(enlace.get('href')) for enlace in soup.find_all('a')]
        print(enlaces)

        # Extraer todo el contenido de la pagina de texto
        all_text = soup.get_text()
        print(all_text)

        # Extraer el texto del elemento main 
        main_text = soup.find('main').get_text()
        print(main_text)

        # Extraer de la id mw-content-text
        content_text = soup.find_all('div', {id: 'mw-content-text'}).get_text()
        print(content_text)

        # Extraer el open graph si existe
        og_image = soup.find('meta', {'property': 'og:image'})
        if og_image:
            print(og_image['content'])
        else:
            print('No se encontro la imagen')

        # tecnicamente lo mismo
        og_image = soup.find('meta', property='og:image')
        if og_image:
            print(og_image['content'])
        else:
            print('No se encontro la imagen')
scrape_url(url)