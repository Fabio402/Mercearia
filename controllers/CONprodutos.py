from models.produtos import *
from models.categoria import *
from DAOs.DAOprodutos import *
from DAOs.DAOcategoria import *
from views.viewProdutos import *

class ConProdutos:
    @classmethod
    def add(cls, produto:Produto):
        while True:
            try:
                cat = DaoCategoria.read()
                if type(cat) != 'list':
                    print('Antes de cadastrar um produto, é preciso cadastrar uma categoria')
                    break
                prod = ViewProdutos.add(cat)
                produtos = DaoProdutos.read()
                produto.prodId = len(produtos)
                DaoProdutos.save(produto)
                print('Produto salvo no ID:', id)
                break
            except:
                print('Não foi possivel salvar o seu produto, tente novamente!')

    @classmethod
    def alter(cls):
        categorias = DaoCategoria.read()
        produtos = DaoProdutos.read()
        while True:
            try:
                alter = int(ViewProdutos.getId())
                for prod in produtos:
                    if prod.prod.id == alter:
                        produto = prod
                if produto != None:
                    produto = ViewProdutos.alter(produto, categorias)

                    break
                else:
                    print('Não foi possivel localizar o produto informado!')

            except:
                print('Não foi possivel localizar o produto informado!')

    @classmethod
    def delete(cls):
        produtos = DaoProdutos.read()
        try:
            aux = True
            request = ViewProdutos.getId()
            delete = ViewProdutos.delete()
            if delete == 's':
                for prod in produtos:
                    if prod.prod.id == request:
                        prod.ativo == False
                        aux = False

                if aux == True:
                    print('Produto não encontrado!')
                else:
                    print('Produto deletado!')
            elif delete == 'n':
                print('O produto não será deletado!')
            else:
                print('Não foi possivel determinar se você quer ou não deletar o produto.')
        except:
            print('Não foi possivel deletar o produto!')