import random

#Entrada
entrada = input('Olá! Vamos jogar pedra, papel ou tesoura? ')

#Processamento
if entrada == 'sim':

    opcoes = ['pedra', 'papel', 'tesoura']
    print(opcoes)

    jogador = input('Escolha: ').strip().lower()
    computador = random.choice(opcoes)
    print(f'Computador escolheu: {computador}')

else:
    print('Que pena! Até a próxima.')
    exit()

#Resultado
if jogador == computador:
    print('Empate!')

elif (jogador == 'pedra' and computador == 'tesoura') or \
     (jogador == 'papel' and computador == 'pedra') or \
     (jogador == 'tesoura' and computador == 'papel'):
    print('Você ganhou!')

else:
    print('Computador ganhou!')
