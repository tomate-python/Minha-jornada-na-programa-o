import time

while True:
    seleção = input('O que você deseja fazer? \n(1) Reajuste salarial \n(2) Desconto salarial \nDigite 1 ou 2: ')
    
    if seleção == '1':
        salario = float(input('Digite o salario do funcionario: R$ ' ))
        time.sleep(1)
        reajuste = float(input('Digite o percentual de reajuste:  %'))
        novo_salario = salario + (salario * reajuste / 100)
        time.sleep(1)
        print('O novo salario do funcionario sera de R$ {:.3f}'.format(novo_salario))
        break

    elif seleção == '2':
        salario = float(input('Digite o salario do funcionario: R$ ' ))
        time.sleep(1)
        desconto = float(input('Digite o percentual de desconto:  %'))
        novo = salario - (salario * desconto / 100)
        time.sleep(1)
        print('O novo salario do funcionario sera de R$ {:.3f}' .format(novo))
        break

    else:
        while True:
         if seleção not in ['1', '2']:
            print('Seleção inválida! Por favor, escolha 1 ou 2.')
            time.sleep(2)
            break
