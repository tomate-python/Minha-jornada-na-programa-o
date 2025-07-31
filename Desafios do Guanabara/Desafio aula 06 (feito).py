#primeira interação (criar um sistema que pergunte o nome etc e formate a data de nascimento ex:29/11/2010 )

#exercicio 1 introdução
nome = input('Qual é seu nome?')
idade = input('Quantos anos você tem?')
altura = input('Qual sua altura?')
data = input('Qual sua data de nascimento?')

#exercicio 2 saida
print('Prazer', nome, 'você nasceu em', data, 'ou seja você tem', idade, 'e Tem', altura, 'metros de altura')

#exercicio 3 soma de numeros
n1 = int(input('Digite um número'))
n2 = int(input('Escolha mais um e descubra a soma deles!'))

print('A soma é {}' .format(n1 + n2))