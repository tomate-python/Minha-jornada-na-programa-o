import random
import time


#Introdução
print('Bem-Vindo ao Jogo de adivinhação de número!')
time.sleep(1)
print('Você tem 5 tentativas para adivinhar o número entre 1 a 10.')

#Geração de numero
secret_number = random.randint(1, 10)

#Tentativas
attempts = 5
time.sleep(1)
while attempts > 0:
    guess = int(input('Digite seu palpite: '))

    if guess < 1 or guess > 10:
        print('Por favor, escolha um número entre 1 a 10.')
        continue
    if guess == secret_number:
        print('Parabéns você acertou!')
        break
    elif guess < secret_number:
        attempts -= 1
        print(f'Errado! Você ainda tem {attempts} tentativas.')
    else:
        print('Errado! Você não tem mais tentativas. O número era:', secret_number)