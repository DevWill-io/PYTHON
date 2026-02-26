# Entrada de dados (mantendo o seu início e adicionando a umidade)
c1 = input('Digite primeira cidade: ')
t1 = float(input(f'Digite a temperatura (°C) de {c1}: '))

c2 = input('Digite a segunda cidade: ')
t2 = float(input(f'Digite a temperatura (°C) de {c2}: '))

c3 = input('Digite a terceira cidade: ')
t3 = float(input(f'Digite a temperatura (°C) de {c3}: '))

# 1. Função de conversão para Fahrenheit
# A fórmula é: F = (C * 9/5) + 32
f1 = (t1 * 9/5) + 32
f2 = (t2 * 9/5) + 32
f3 = (t3 * 9/5) + 32

# 2. Lógica para definir a cidade mais quente
if t1 >= t2 and t1 >= t3:
    mais_quente = c1
    temp_max_f = f1
elif t2 >= t1 and t2 >= t3:
    mais_quente = c2
    temp_max_f = f2
else:
    mais_quente = c3
    temp_max_f = f3

# 3. Exibição dos resultados com alerta de cor
print("-" * 30)
print(f"A cidade mais quente é: {mais_quente} ({temp_max_f:.1f}°F)")
print("-" * 30)