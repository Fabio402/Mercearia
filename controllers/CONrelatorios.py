from models.produtos import *
from controllers.CONprodutos import *
from models.vendas import *
from controllers.CONvendas import *
from models.pessoas import *
from controllers.CONpessoas import *
class ConRelatorios:
    @classmethod
    def geral(cls):
        try:
            rel = []
            produtos = ConProdutos.list()
            for produto in produtos:
                if produto.ativo == True:
                    rel.append([produto.prodId, produto.nome, produto.qtd])
            return rel
        except Exception as e:
            return e
    @classmethod
    def data(cls, data):
        try:
            rel = []
            vendas = ConVendas.list()
            for venda in vendas:
                if venda.ativo == True:
                    if str(venda.data) == str(data):
                        rel.append([venda.vendasId, venda.precoFinal])
            return rel
        except Exception as e:
            return e
    @classmethod
    def maisVendidos(cls):
        try:
            rel = []
            vendas = ConVendas.list()
            produtos = ConProdutos.list()
            for produto in produtos:
                cont = 0
                if produto.ativo == True:
                    for venda in vendas:
                        print(venda.vendasId)
                        if venda.ativo == True:
                            for item in venda.itensId:
                                print(cont)
                                if produto.prodId == item:
                                    cont += 1
                    rel. append([produto.nome, cont])
            rel = sorted(rel, key=lambda x: x[1], reverse=True)
            return rel
        except Exception as e:
            return e
    @classmethod
    def clientes(cls):
        try:
            rel = []
            vendas = ConVendas.list()
            clientes = ConClientes.list()
            for cliente in clientes:
                cont = 0
                if cliente.ativo == True:
                    for venda in vendas:
                        if venda.ativo == True:
                            if cliente.cliId == venda.cliente:
                                    cont += 1
                rel.append([cliente.nome, cont])
            rel = sorted(rel, key=lambda x: x[1], reverse=True)
            return rel
        except Exception as e:
            return e
