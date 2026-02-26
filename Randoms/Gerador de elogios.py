#O programa pede o nome de uma pessoa e sorteia um elogio diferente de uma lista (como "Gênio", "Dedicado" ou "Criativo") para exibir na tela.

import random

elogios = ["gentil", "bom", "fiel", "puro", "doce", "leal", "raro", "belo", "luz", "paz", "real", "nato", "vivo", "leve", "sutil", "fino", "sábio", "justo", "noite", "claro", "nato", "único", "firme", "hábil", "capaz", "limpo", "bravo", "grato", "forte", "mimo"]

nome = input('Qual seu nome? ').title()

# Primeiro elogio automático
vc = random.choice(elogios)
print(f'{nome} Você é {vc}')

# Variável de controle para o loop
continuar = True

while continuar:
    dn = input('\nQuer outro elogio? (sim/não): ').lower()

    if 'sim' in dn:
        vc = random.choice(elogios)
        print(f'{nome} Você é {vc}!')
    else:
        print('Poxa, tudo bem. Até a próxima! 👋')
        continuar = False # Isso quebra o loop
