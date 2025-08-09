lista = ['Minions', 'Vingadores', 'One Piece']


#Sistema de lista de votação
while True:
    print('Digite o filme que gostaria de adicionar (ou "sair" para encerrar):')
    filme = input()
    if filme.lower() == 'sair':
        break
    elif filme:
        print(f'Você adicionou o filme: {filme}')
        lista.append(filme)

votos = [0] * len(lista)

while True:
    print('Vote no filme que deseja assistir: ')
    for idx, filme in enumerate(lista, 1):
        print(f'{idx} - {filme}')
    print(f'Digite o número do filme (1 a {len(lista)}), ou "fim" para encerrar: ')

    voto = input()
    if voto.lower() == 'fim':
        break
    if voto.isdigit() and 1 <= int(voto) <= len(lista):
        votos[int(voto) - 1] += 1
        print(f'Você votou em: {lista[int(voto) - 1]}')
    else:
        print(f'Voto inválido. Por favor, digite um número entre 1 e {len(lista)}.')

vencedor = votos.index(max(votos))
print('🎬 O filme mais votado foi:', lista[vencedor])