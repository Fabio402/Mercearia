from models.vendas import *
from DAOs.DAOvendas import *
from datetime import date
from controllers.CONprodutos import *

class ConVendas:
    @classmethod
    def price(cls, lista: list):
        try:
            total = 0
            produtos = DaoProdutos.read()
            for i in lista:
                for produto in produtos:
                    if int(i) == int(produto.prodId):
                        total += float(produto.venda)
            return total
        except Exception as e:
            return e
    @classmethod
    def sellEstoque(cls, lista: list):
        produtos = DaoProdutos.read()
        for i in lista:
            for produto in produtos:
                if int(i) == int(produto.prodId):
                    produto.qtd -= 1
                    ConProdutos.alter(produto.prodId, produto)
    @classmethod
    def undoEstoque(cls, lista: list):
        produtos = DaoProdutos.read()
        for i in lista:
            for produto in produtos:
                if int(i) == int(produto.prodId):
                    produto.qtd += 1
                    ConProdutos.alter(produto.prodId, produto)
    @classmethod
    def list(cls):
        try:
            vendas = DaoVendas.read()
            vend = []
            for venda in vendas:
                if venda.ativo == True:
                    vend.append(venda)
            return vend
        except Exception as e:
            return (e)
    @classmethod
    def listToday(cls):
        try:
            hoje = str(date.today())
            vendas = DaoVendas.read()
            vendasHoje = []
            for venda in vendas:
                if venda.data == hoje:
                    vendasHoje.append(venda)
            return vendasHoje
        except Exception as e:
            return e
    @classmethod
    def add(cls, funcId, cliId, prodIds, preco, desconto):
        try:
            vendas = DaoVendas.read()
            venda = Vendas(len(vendas), funcId, cliId, prodIds, preco, desconto, int(preco)-int(desconto), date.today(), '1')
            DaoVendas.save(venda)
            ConVendas.sellEstoque(prodIds)
            return f'A venda nº {len(vendas)} foi salva com sucesso!'
        except Exception as e:
            print(e)
    @classmethod
    def alter(cls, alterId, venda: Vendas):
        try:
            DaoVendas.alter(alterId, venda)
            ConVendas.sellEstoque(venda.itensId)
            if venda.ativo == False:
                ConVendas.undoEstoque(venda.itensId)
            return "Venda alterada alterado!"
        except Exception as e:
            print(e)