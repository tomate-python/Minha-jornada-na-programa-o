preço = float(input('Qual o preço do produto R$:'))

des = int(input('Qual o desconto %:'))

valor = preço - (preço*des/ 100)
print('O valor de R${} foi para R${}' .format(preço, valor))