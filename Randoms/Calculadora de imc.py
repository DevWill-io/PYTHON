# Entrada de dados
peso = float(input('Qual o seu Peso (kg)? '))
altura = float(input('Qual a sua altura (m)? '))

# Cálculo do IMC
imc = peso / (altura ** 2)

print(f'\nSeu IMC é: {imc:.2f}')

# Classificação
if imc < 18.5:
    print('Classificação: Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Classificação: Peso ideal (parabéns!)')
elif 25 <= imc < 30:
    print('Classificação: Sobrepeso')
elif 30 <= imc < 35:
    print('Classificação: Obesidade Grau I')
elif 35 <= imc < 40:
    print('Classificação: Obesidade Grau II (severa)')
else:
    print('Classificação: Obesidade Grau III (mórbida)')



