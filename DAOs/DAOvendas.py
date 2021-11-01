from models.vendas import *
from datetime import datetime
class DaoVendas:
    @classmethod
    def save(cls, venda: Vendas):
            with open('../DAOs/data/vendas.txt', 'a') as file:
                if venda.ativo == True:
                    venda.ativo = '1'
                else:
                    venda.ativo = '0'
                file.writelines(str(venda.vendasId) +'|'+ str(venda.vendedor) +'|'+ str(venda.cliente) +'|')
                file.writelines(str(venda.itensId))
                file.writelines('|'+ str(venda.precoTotal) +'|'+ str(venda.desconto) +'|'+ str(venda.precoFinal) +'|'+ str(venda.data) +'|'+ str(venda.ativo)+'\n')
    @classmethod
    def read(cls):
        with open('../DAOs/data/vendas.txt', 'r') as file:
            aux = file.readlines()
            aux = list(map(lambda data: data.replace('\n',''), aux))
            aux = list(map(lambda data: data.split('|'),aux))
            cls.vendas = []
            for i in aux:
                aux = []
                for j in i[3]:
                    try:
                        aux.append(int(j))
                    except:
                        continue
                venda = Vendas(int(i[0]), int(i[1]), int(i[2]), aux, float(i[4]), float(i[5]), float(i[6]),  i[7], i[8])
                cls.vendas.append(venda)
        return cls.vendas

    @classmethod
    def alter(cls, alterId, alteracao: Vendas):
        vendas = DaoVendas.read()
        vend = list(map(lambda data: alteracao if (data.vendasId == alterId) else (data), vendas))
        with open('../DAOs/data/vendas.txt', 'w') as file:
            for i in vend:
                if i.ativo == True:
                    i.ativo = '1'
                else:
                    i.ativo = '0'
                file.writelines(str(i.vendasId) +'|'+ str(i.vendedor) +'|'+ str(i.cliente) +'|')
                file.writelines(str(i.itensId))
                file.writelines('|'+ str(i.precoTotal) +'|'+ str(i.desconto) +'|'+ str(i.precoFinal) +'|'+ str(i.data) +'|'+ str(i.ativo)+'\n')
