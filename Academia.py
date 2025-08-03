import time

#Entrada do aluno
print(f'Seja Bem-vindo à Academia!')
print(f'Vamos começar com algumas perguntas para personalizar seu treino. ')


time.sleep(1)
name = input(f'Qual é seu nome? ')
time.sleep(3)
peso = float(input(f'Qual é seu peso em Kg?'))
time.sleep(3)
altura = float(input('Qual é sua altura em metros? '))
time.sleep(3)
idade = int(input('Qual é sua idade? '))


#calculando o IMC
imc = peso / (altura ** 2)
if imc <18.5:
    print(f'{name}, seu IMC é {imc:.2f}, o que indica que você está abaixo do peso ideal.')
elif 18.5 <= imc < 24.9:
    print(f'{name}, seu IMC é ideal, com um valor de {imc:.2f}.')
elif 25 <= imc < 29.9:
    print(f'{name}, seu IMC é {imc:.2f}, o que indica sobrepeso.')
elif 30 <= imc < 49.9:
    print(f'{name}, seu IMC é {imc:.2f}, o que indica obesidade.')
else:
    print(f'{name}, seu IMC é {imc:.2f}, o que indica obesidade mórbida.')

