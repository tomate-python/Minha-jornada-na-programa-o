👨‍💻 Desafio 003 – Somando Dois Valores

📋 Explicação: Aplicação que realiza a soma entre dois números digitados pelo usuário.

🧠 Lógica geral: Recebe dois valores → Converte para tipo numérico → Soma → Exibe o resultado.

📂 Código:

python
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite mais um e descubra a soma deles: '))
result = n1 + n2
print('Resultado: {}'.format(result))

🔽=================================================================🔽
👨‍💻 Desafio 004 – Analisador de String

📋 Explicação: Verifica diversas propriedades de uma string digitada pelo usuário.

📂 Código:

python
import time

algo = input('Digite algo: ')
print('Aqui estão as informações sobre:')
time.sleep(1)
print('Tipo primitivo:', type(algo))
time.sleep(0.5)
print('É alfanumérico:', algo.isalnum())
time.sleep(0.5)
print('É alfabético:', algo.isalpha())
time.sleep(0.5)
print('Só contém espaços:', algo.isspace())
time.sleep(0.5)
print('É número:', algo.isnumeric())
time.sleep(0.5)
print('Está em maiúsculas:', algo.isupper())
time.sleep(0.5)
print('Está em minúsculas:', algo.islower())
time.sleep(0.5)
print('Está capitalizada:', algo.istitle())

🔽=================================================================🔽
👨‍💻 Desafio 005 – Antecessor e Sucessor

📋 Explicação: Recebe um número e exibe seu antecessor e sucessor.

📂 Código:

python
p1 = int(input('Digite um número: '))
print('Seu antecessor é', p1 - 1, 'e seu sucessor é', p1 + 1)

🔽=================================================================🔽
👨‍💻 Desafio 006 – Dobro, Triplo e Raiz Quadrada

📋 Explicação: Recebe um número e calcula seu dobro, triplo e raiz quadrada.

📂 Código:

python
import math

n = int(input('Digite um número: '))
input('Pressione "Enter" para continuar...')
print('O dobro é:', n * 2) 
print('O triplo é:', n * 3)
print('A raiz quadrada é:', math.sqrt(n))

🔽=================================================================🔽
👨‍💻 Desafio 007 – Média de Notas

📋 Explicação: Calcula a média aritmética entre duas notas fornecidas pelo usuário.

📂 Código:

python
print('Bem-vindo ao calculador de média')
nt1 = float(input('Digite sua nota: '))
nt2 = float(input('Digite a outra nota: '))
media = (nt1 + nt2) / 2
print('Sua média final é {:.1f}'.format(media))

🔽=================================================================🔽
👨‍💻 Desafio 008 – Conversão de Medidas

📋 Explicação: Converte uma medida em metros para centímetros e milímetros.

📂 Código:

python
vlr = float(input('Digite uma medida em metros: '))
cm = vlr * 100
mm = vlr * 1000
print('O valor {}m corresponde a {:.0f} centímetros e {:.0f} milímetros'.format(vlr, cm, mm))
