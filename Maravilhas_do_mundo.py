import requests
from bs4 import BeautifulSoup

html = requests.get('https://brasilescola.uol.com.br/curiosidades/'
                    'candidatas-as-sete-maravilhas-mundo-contemporaneo.htm')

# verifica se o status code foi bem sucedido
if html.status_code == 200:
    print('Requisição concluida com sucesso! \n')

    # Fornece ao bs4 a página e modo de leitura

    soup = BeautifulSoup(html.content, 'html.parser')

    # Procura todos as tags Strong e retorna printando cada item da lista
    [print(maravilha.get_text()) for maravilha in soup.find_all('strong')]
else:
    print('Não foi possivél receber as informações da página requirida')