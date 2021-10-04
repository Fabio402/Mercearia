from models.produtos import *
class ViewProdutos:
    @classmethod
    def add(cls,id,categorias):
        print('Preencha as seguintes informações.\n')
        nome = input('Nome:')
        qtd = input('Quantidade em estoque:')
        precoVenda = input('Preço para vender o item:')
        precoCusto = input('Preço de custo do item:')
        for categoria in categorias:
            print(categoria.serial+'-', categoria.nome+'\n')
        cat = input('Informe o numero que representa a categoria:')
        return Produto(nome,id,qtd,precoVenda,precoCusto,cat)

    @classmethod
    def delete(cls):
        return input('Tem certeza que deseja excluir este produto?(S/N)').lower()

    @classmethod
    def getId(cls):
        return input('Digite o código do produto que deseja editar:')

    @classmethod
    def alter(cls, produto: Produto, categorias):
        print('Preencha as seguintes informações.\n')
        produto.nome = input('Nome:')
        produto.qtd = input('Quantidade em estoque:')
        produto.precoVenda = input('Preço para vender o item:')
        produto.precoCusto = input('Preço de custo do item:')
        for categoria in categorias:
            print(categoria.serial + '-', categoria.nome + '\n')
        produto.categoria = input('Informe o numero que representa a categoria:')
        if produto.ativo == True:
            x = input('Deseja desativar o produto?(S/N)').lower()
            if x =='s':
                produto.ativo = False
        else:
            x = input('Deseja ativar o produto?(S/N)').lower()
            if x == 's':
                produto.ativo = True
        return produto