import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.python.org")

soup = BeautifulSoup(html.content, 'html.parser')

div_use_for = soup.find('div', attrs={'class': 'medium-widget applications-widget last'})

base = []
for item in div_use_for.find_all('li'):
    print(item.b.string)

    for biblio in item.span.contents:
        biblio = str(biblio.string).replace(',', ' ').strip('\n').strip(' ')
        if biblio != '' and '\n':
            print(' ' * 3, biblio)
            base.append(biblio)

    print()

