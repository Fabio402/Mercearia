from models.produtos import *
from models.categoria import *
from DAOs.DAOprodutos import *
from DAOs.DAOcategoria import *
from views.viewProdutos import *

class ConProdutos:
    @classmethod
    def add(cls):
        categorias = DaoCategoria.read()
        while True:
            try:
                produtos = DaoProdutos.read()
                id = len(produtos)
                request = ViewProdutos.add(id, categorias)
                DaoProdutos.save(request)
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