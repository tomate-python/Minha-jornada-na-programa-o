largura = float(input ('Qual a largura da parede:'))
altura = float(input('Qual a altura da parede:'))
area = largura * altura
print('Sua parede tem dimensão {:.2f} x {:.2f} e sua aréa é de {}m²' .format(largura, altura, area))
tinta = area / 2
print('Para pintar a parede você precisará de: {}L' .format(tinta))