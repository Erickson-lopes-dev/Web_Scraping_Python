import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from tqdm import tqdm

palavra = 'diabo'

# Página principal com todas as musicas dos artistas
html = requests.get('https://www.vagalume.com.br/raul-seixas/')

# Estruturando dados como html
soup = BeautifulSoup(html.content, 'html.parser')

links = []

# Procura a lista alfabetica e filtra todos as tags a
for tag in soup.find(id='alfabetMusicList').find_all('a'):
    # Por cada tag pega o conteúdo do atributo href
    caminhno = tag.attrs['href']
    # filtra os links para que não sej adicionado os links com #play no final
    if '#play' not in str(caminhno):
        # Gera o link para acessar a música e adiciona na lista
        links.append('https://www.vagalume.com.br' + caminhno)
        # # printa para exibir o caminho completo
        # print('https://www.vagalume.com.br' + caminhno)

frases = []
for link_musica in tqdm(links):
    html_musica = requests.get(link_musica)
    soup = BeautifulSoup(html_musica.content, 'html.parser')

    # # printa um objeto bs4 com toda a letra da musica
    # print(soup.find(id="lyrics").contents)

    try:
        for linhas in soup.find(id="lyrics").contents:
            if palavra.lower() in str(linhas).lower():
                frases.append(
                    dict(musica=soup.find(id="lyricContent").find('h1').string, frase=str(linhas).lower())
                )
                print(soup.find(id='lyricContent').find('h1').string, ':')
                print(f'{" " * 3 + linhas}. \n')
    except AttributeError as err:
        pass

print('\n'*3)
#

tabela_final = PrettyTable(['Música', 'Frase a Palavra encontrada'])

[tabela_final.add_row([str(i['musica']), str(i['frase'])]) for n, i in enumerate(frases) if i not in frases[n + 1:]]

print(tabela_final)


