import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.python.org")

soup = BeautifulSoup(html.content, 'html.parser')

div_use_for = soup.find('div', attrs={'class': 'medium-widget applications-widget last'})

base = []
for item in div_use_for.find_all('li'):
    print(item.b.string)

    for biblio in item.span.contents:

        try:
            href = biblio['href']
        except TypeError as err:
            pass

        biblio = str(biblio.string).replace(',', ' ').strip('\n').strip(' ')
        if biblio != '':
            print(' ' * 3, f'{biblio:<10} {href}')

    print()

# [print(a) for a in soup.find_all('a', attrs={'class': 'tag'})]
