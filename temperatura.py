import requests
from bs4 import BeautifulSoup

html = requests.get("https://pt.wikipedia.org/wiki/Wikipédia:Página_principal")

soup = BeautifulSoup(html.content, 'html.parser')

temperatura = soup.find_all('div', {'class': 'main-page-block-heading'})

print(temperatura)
