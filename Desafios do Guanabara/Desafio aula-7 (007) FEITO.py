#Um programa que leia 2 notas de um aluno e calcule sua media

print('Bem-vindo ao calculador de média')
nt1 = float(input('Digite sua nota:'))
nt2 = float(input('Digite a outra nota'))

#Calculo da nota
media = (nt1+nt2)/2
print('Sua média final é {:.1f}'.format(media))