from prettytable import PrettyTable
from tqdm import tqdm

frase = [
    {'musica': 'Anarkilópolis', 'frase': 'pra o diabo, os que me chamaram aqui'},
    {'musica': 'Capim Guiné', 'frase': 'eu tô virado do diabo, eu tô retado cum você'},
    {'musica': 'Conversa Pra Boi Dormir', 'frase': 'que o diabo fez, enquanto deus marcou'},
    {'musica': 'D.D.I. (discagem Direta Inter-estelar)', 'frase': 'que o diabo diz que vai baixar de uma vez por aí'},
    {'musica': 'D.D.I. (discagem Direta Inter-estelar)', 'frase': 'pode ser um trote do diabo'},
    {'musica': 'Eu Sou Eu, Nicuri é O Diabo', 'frase': 'eu sou eu, nicuri é o diabo,'},
    {'musica': 'Eu Sou Eu, Nicuri é O Diabo', 'frase': 'eu sou eu, nicuri é o diabo.'},
]

print(frase)

tabela_final = PrettyTable(['Música', 'Frase com a palavra procurada'])

[tabela_final.add_row([i['musica'], i['frase']]) for n, i in enumerate(frase) if i not in frase[n + 1:]]

print(tabela_final)
