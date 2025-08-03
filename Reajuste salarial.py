import time


selecao = None
entrada_correta = False

#Entrada do usuario
print('Bem vindo ao sistema de reajuste salarial!')
time.sleep(1)

while not entrada_correta:
    time.sleep(1)
    selecao = input('O que você deseja fazer? \n(1) Reajuste salarial \n(2) Desconto salarial \nDigite 1 ou 2: ')
    entrada_correta = selecao in['1', '2']

    if not entrada_correta:
        print('Opção invalida. Por favor, digte 1 ou 2.')


#Calulos
if selecao == '1':
    print('Você escolheu reajuste salaral')
    time.sleep(1)
    salario = float(input('Digite o salario do funcionario: R$ '))
    reajuste = float(input('Digite o percentual de reajuste: %'))
    novo_salario = salario + (salario * reajuste / 100)
    print('O novo salario do funcionario é: R$ {:.3f}'.format(novo_salario))

else:
    print('Você escolheu desconto salarial')
    time.sleep(1)
    salario2 = float(input('Digite o salario do funcionario: R$ '))
    desconto = float(input('Digite o percentual de desconto> % '))
    novo_salario2 = salario2 - (salario2 * desconto / 100)





    