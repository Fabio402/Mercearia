from models.produtos import *

class DaoProdutos:
    @classmethod
    def save(cls, produto: Produto):
        with open('data/produtos.txt','a') as file:
            if produto.ativo == True:
                produto.ativo = '1'
            else:
                produto.ativo = '0'
            file.writelines(str(produto.prodId) +'|'+ produto.nome +'|'+ produto.categoria +'|'+ str(produto.qtd) +'|'+ str(produto.custo) +'|'+ str(produto.venda)+'|'+ produto.ativo +'\n')

    @classmethod
    def read(cls):
        with open('data/produtos.txt', 'r') as file:
            aux = file.readlines()
            aux = list(map(lambda data: data.replace('\n',''), aux))
            aux = list(map(lambda data: data.split('|'),aux))
            cls.produtos = []
            for i in aux:
                produto = Produto(i[1],int(i[0]),int(i[3]),float(i[5]),float(i[4]),i[2],i[6])
                cls.produtos.append(produto)

        return cls.produtos