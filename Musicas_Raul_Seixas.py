import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.vagalume.com.br/raul-seixas/')
#
# soup = BeautifulSoup(html.content, 'html.parser')
#
# links = []
#
# for tag in soup.find(id='alfabetMusicList').find_all('a'):
#     caminhno = tag.attrs['href']
#     if '#play' not in str(caminhno):
#         links.append('https://www.vagalume.com.br' + caminhno)
#
# print(links)
#
# html = requests.get('https://www.vagalume.com.br/raul-seixas/o-dia-em-que-a-terra-parou.html')
#
# soup = BeautifulSoup(html.content, 'html.parser')
#
# # print(soup.find(id="lyrics").contents)
#
# palavra = 'não tava lá'
#
# for linhas in soup.find(id="lyrics").contents:
#     if palavra in str(linhas):
#         print(linhas)
#
#     # if str(linhas) != '<br/>':
#     #     print(linhas)


soup = BeautifulSoup(html.content, 'html.parser')

links = []

for tag in soup.find(id='alfabetMusicList').find_all('a'):
    caminhno = tag.attrs['href']
    if '#play' not in str(caminhno):
        links.append('https://www.vagalume.com.br' + caminhno)

for link_musica in links:
    html_musica = requests.get(link_musica)
    soup = BeautifulSoup(html_musica.content, 'html.parser')

    # print(soup.find(id="lyrics").contents)

    palavra = 'jesus'

    try:
        for linhas in soup.find(id="lyrics").contents:
            if palavra in str(linhas):
                print(linhas)
    except AttributeError as err:
        pass

