import requests
from bs4 import BeautifulSoup

# Pagina
html = requests.get("https://www.python.org")

soup = BeautifulSoup(html.content, 'html.parser')

# captura a div com todos os objetos desejados
div_use_for = soup.find('div', attrs={'class': 'medium-widget applications-widget last'})

# filtra as tags li / que separa
for item in div_use_for.find_all('li'):
    # printa cada area de atuação do python
    print(item.b.string)

    # Exibe as bibliotecas de cada area
    for biblio in item.span.contents:
        href = ''
        # função a baixo busca os links de cada biblioteca
        try:
            href = biblio['href']
        except TypeError as err:
            pass

        # Raspagem de dados para que elimine as linhas, espaços e virgulas
        biblio = str(biblio.string).replace(',', ' ').strip('\n').strip(' ')
        # Na lista ainda sobra um item vazio
        if biblio != '':
            print(' ' * 3, f'{biblio:<10} {href}')

    print()

