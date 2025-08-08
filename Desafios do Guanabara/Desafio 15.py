#Desafio: Aluguel de carros

#Entrada de dados
dias_aluguel = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))

#Cálculo do valor a pagar
valor = (dias_aluguel * 60) + (km_rodados * 0.15)

#saida dados
print(f'Com base nas informações fornecidadas: \n Dias: {dias_aluguel} \n Km rodados: {km_rodados} \n O valor a pagar é de R$ {valor:.2f}')
print('Obrigado por alugar conosco! Volte sempre!')