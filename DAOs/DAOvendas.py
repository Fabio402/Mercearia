from models.vendas import *

class DaoVendas:
    @classmethod
    def save(cls, venda: Vendas):
        if os.path.isdir('data/vendas.txt'):
            with open('data/vendas.txt', 'a') as file:
                if venda.ativo == True:
                    venda.ativo = '1'
                else:
                    venda.ativo = '0'
                file.writelines(str(venda.vendasId) +'|'+ str(venda.vendedor) +'|'+ str(venda.cliente) +'|')
                file.writelines(str(venda.itensId))
                file.writelines('|'+ str(venda.precoTotal) +'|'+ str(venda.desconto) +'|'+ str(venda.precoFinal) +'|'+ str(venda.ativo)+'\n')
        else:
            os.makedirs('data')
            Daovendas.save(venda)
    @classmethod
    def read(cls):
        with open('data/vendas.txt', 'r') as file:
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
                venda = Vendas(int(i[0]),int(i[1]),int(i[2]),float(i[4]),float(i[5]),float(i[6]),i[7],aux)
                cls.vendas.append(venda)

        return cls.vendas
produtos = [0,1,2,3]
venda = Vendas(0,1,0, 20.00, 2.00,18.00 ,True, produtos)
DaoVendas.save(venda)

vendas = DaoVendas.read()
for venda in vendas:
    print(venda.vendasId, venda.vendedor, venda.cliente)
    print(venda.itensId)