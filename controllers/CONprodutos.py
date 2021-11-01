from models.produtos import *
from models.categoria import *
from DAOs.DAOprodutos import *
from DAOs.DAOcategoria import *
from views.viewProdutos import *

class ConProdutos:
    @classmethod
    def add(cls, nome,qtd,precoVenda,precoCusto,cat):
            try:
                produtos = DaoProdutos.read()
                produto = Produto(nome,len(produtos), qtd, precoVenda, precoCusto, cat)
                DaoProdutos.save(produto)
                return 'Produto salvo!'
            except Exception as e:
                print(e)
    @classmethod
    def list(cls):
        try:
            produtos = DaoProdutos.read()
            return produtos
        except Exception as e:
            return e
    @classmethod
    def alter(cls, id, produto: Produto):
        try:
            DaoProdutos.alter(id, produto)
            return "Produto alterado!"
        except Exception as e:
            print(e)
    @classmethod
    def delete(cls, id, produto: Produto):
            try:
                DaoProdutos.alter(id, produto)
                return "Produto deletado!"
            except Exception as e:
                print(e)