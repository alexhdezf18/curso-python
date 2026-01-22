from playwright.sync_api import sync_playwright

url = 'https://midu.dev'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto(url)

    # Recueperar el primer articulo
    first_article_anchor = page.locator('article a').first
    first_article_anchor.click()

    # Esperar a que la pagina cargue
    page.wait_for_load_state()

    # Recuperar la primer imagen
    first_image = page.locator('main img').first
    image_src = first_image.get_attribute('src')
    print(f"La imagen del primer es: {image_src}")

    # Encontrar elementos apartir del xPath
    first_image = page.locator('xpath=/html/body/main/div[1]/img')
    print(first_image.get_attribute('src'))

    curso_content_container = page.locator('text="Contenido del curso"')
    curso_content_sibling = curso_content_container.locator('xpath=./div/')

    browser.close()