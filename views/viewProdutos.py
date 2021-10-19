from models.produtos import *
from controllers.CONprodutos import *
from controllers.CONcategorias import *
class ViewProdutos:
    @classmethod
    def add(cls):
        categorias = ConCategorias.list()
        print('Preencha as seguintes informações.\n')
        nome = input('Nome:')
        qtd = input('Quantidade em estoque:')
        precoVenda = input('Preço para vender o item:')
        precoCusto = input('Preço de custo do item:')
        for cat in categorias:
            if cat.ativo == True:
                print(f"{cat.serial}- {cat.nome}.")
        cat = input('Informe o numero que representa a categoria:')
        aux = ConProdutos.add(nome, qtd, precoVenda, precoCusto, cat)
        print(aux)
    @classmethod
    def alter(cls):
        print('Estes são os produtos cadastrados:')
        produtos = ConProdutos.list()
        for produto in produtos:
            if produto.ativo == True:
                print(f'{produto.prodId} - {produto.nome}')
        id = input('Insira o numero do produto que deseja alterar: ')
        produto: Produto
        for prod in produtos:
            if prod.prodId == id:
                produto = Produto(prod.nome, prod.prodId ,prod.qtd ,prod.venda ,prod.custo, prod.categoria, '1')
                break
        aux = input('Deseja alterar o nome?(S/N)').lower()
        if aux == 's':
            produto.nome = input('Nome:')
            aux = 'n'
        aux = input('Deseja alterar o preço de venda?(S/N)').lower()
        if aux == 's':
            produto.venda = input('Preço: ')
            aux = 'n'
        aux = input('Deseja alterar o preço que o produto foi comprado?(S/N)').lower()
        if aux == 's':
            produto.custo = input('Preço: ')
            aux = 'n'
        aux = input('Deseja alterar a quantidade de estoque?(S/N)').lower()
        if aux == 's':
            produto.qtd = input('Quantidade em estoque: ')
            aux = 'n'
        aux = input('Deseja alterar a categoria do produto?(S/N)').lower()
        if aux == 's':
            cat = ConCategorias.list()
            print('As categorias disponiveis são: ')
            for i in cat:
                if i.ativo == True:
                    print(f'{i.serial} - {i.nome}')
            produto.cat = input('Qual o numero da categoria que deseja adicionar?')
            aux = 'n'
        aux = ConProdutos.alter(id, produto)
        print(aux)

    @classmethod
    def delete(cls):
        return input('Tem certeza que deseja excluir este produto?(S/N)').lower()
