#Boas vindas
print('Bem vindo ao conversor de temperatura!')
print('Este é um projeto simples de conversão de temperatura entre Celsius e Fahrenheit. \n Autor: Thomas')

#Entrada de dados
entry = False
selecao = None

while not entry:
    selecao = input(('Escolha entre as opções abaixo: \n (1) Celsius para Fahrenheit \n (2) Fahrenheit para Celsius \n R: '))
    entry = selecao in ['1', '2']

    if not entry:
        print('Opção inválida. Por favor, escolha 1 ou 2.')


#Processamento e saida

#celsius para faren
if selecao == '1':
    print('Você escolheu a opção {}'.format(selecao))
    celsius = float(input('Digite a temperatura em Celsius: '))
    celsius_faren = (celsius * 9 / 5) + 32
    print('A temperatura em Fahrenheit é: {:.2f}'.format(celsius_faren))

#faren para celsius
else:
    print('Você escolheu a opção {}'.format(selecao))
    fahrenheit = float(input('Digite a temperatura em Farenheit: '))
    faren_celsius = (fahrenheit - 32) * 5/9
    print('A temperatura em Celsius é: {:.2f}'.format(faren_celsius))

