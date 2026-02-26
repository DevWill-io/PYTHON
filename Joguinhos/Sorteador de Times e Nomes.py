#Faça um Sorteador de Times/Nomes! É simples e muito útil.
#O que ele faz:
#Recebe uma lista de nomes.
#Embaralha tudo usando import random.
#Divide os nomes em grupos ou escolhe um vencedor

import random

# Lista para armazenar os nomes
times = []

# Usando um loop para evitar repetir 'input' várias vezes
for i in range(1, 11):
    nome = input(f'Digite o nome do {i}º time: ').title()
    times.append(nome)

# Sorteio
time_sorteado = random.choice(times)

print("=" * 30)
print(f'O time que irá começar será o: {time_sorteado}! BOA SORTE!')
print("=" * 30)
