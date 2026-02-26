import random
from time import sleep

# 1. Definições Iniciais
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

# 2. Entrada do Jogador
jogador = int(input('Qual é a sua jogada? '))

if jogador < 0 or jogador > 2:
    print('JOGADA INVÁLIDA! Você deve escolher 0, 1 ou 2.')
else:
 print('JO')
 sleep(0.5)
 print('KEN')
 sleep(0.5)
 print('PÔ!!!')

# 3. Exibição das jogadas
 print('-=' * 11)
 print(f'Computador jogou: {itens[computador]}')
 print(f'Jogador jogou: {itens[jogador]}')
 print('-=' * 11)

# 4. Lógica do Jogo
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')

elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE')

elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE!')