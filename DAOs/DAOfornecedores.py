from models.fornecedores import *
class DaoFornecedores:
    @classmethod
    def save(cls, fornecedor: Fornecedores):
        with open('data/fornecedores.txt','a') as file:
            if fornecedor.ativo == True:
                fornecedor.ativo = '1'
            else:
                fornecedor.ativo = '0'
            file.writelines(str(fornecedor.id) +'|'+ fornecedor.nome +'|'+ fornecedor.cnpj +'|'+ fornecedor.categoria +'|'+ fornecedor.tel +'|'+ fornecedor.ativo +'\n')

    @classmethod
    def read(cls):
        with open('data/fornecedores.txt', 'r') as file:
            aux = file.readlines()
            aux = list(map(lambda data: data.replace('\n',''), aux))
            aux = list(map(lambda data: data.split('|'),aux))
            cls.fornecedores = []
            for i in aux:
                fornecedor = Fornecedores(int(i[0]), i[1], i[2], i[4], i[3], i[5])
                cls.fornecedores.append(fornecedor)

        return cls.fornecedores