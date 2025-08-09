# Lista para armazenar
produtos = []

def listar_produtos():
    if not produtos:
        print('Nenhum produto cadastrado.')
    else:
        print('Produtos cadastrados:')
        for idx, produto in enumerate(produtos, 1):
            print(f'{idx}. {produto["nome"]} - R$ {produto["preco"]:.2f} - {produto["quantidade"]} unidades')

#entrada escolha
while True:
    escolha = input('[1]Cadastrar produto \n[2]Listar produtos \n[3]Buscar produtos \n[4]Sair\nEscolha uma opção: ')

#saida cadastro
    if escolha == '1':
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        quantidade = int(input('Digite a quantidade do produto: '))
        produtos.append({
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        })
        print(f'Produto {nome} cadastrado com sucesso!')

#saida listar
    elif escolha == '2':
        listar_produtos()

#saida busca
    elif escolha == '3':
        termo_busca = input('Digite o nome do produto a ser buscado: ')
        encontrados = [produto for produto in produtos if termo_busca.lower() in produto['nome'].lower()]
        if encontrados:
            print('Produtos encontrados:')
            for produto in encontrados:
                print(f"- {produto['nome']} - R$ {produto['preco']:.2f} - {produto['quantidade']} unidades")
        else:
            print('Nenhum produto encontrado.')
    break

else:
    print('Opção inválida.')