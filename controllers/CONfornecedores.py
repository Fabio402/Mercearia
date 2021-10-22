from DAOs.DAOfornecedores import *
from models.fornecedores import *
class ConFornecedores:
    @classmethod
    def add(cls, nome,cnpj,cat,telefone):
        try:
            fornecedores = DaoFornecedores.read()
            fornecedor = Fornecedores(len(fornecedores), nome, cnpj, cat, telefone)
            DaoFornecedores.save(fornecedor)
            return 'Fornecedor salvo!'
        except Exception as e:
            print(e)

    @classmethod
    def list(cls):
        try:
            fornecedores = DaoFornecedores.read()
            return fornecedores
        except Exception as e:
            print(e)
            return 104

    @classmethod
    def alter(cls, id, fornecedor: Fornecedores):
        try:
            DaoFornecedores.alter(id, fornecedor)
            return "Fornecedor alterado!"
        except Exception as e:
            print(e)
            return 105

    @classmethod
    def delete(cls, id, fornecedor: Fornecedores):
        try:
            DaoFornecedores.alter(id, fornecedor)
            return "Fornecedor deletado!"
        except Exception as e:
            print(e)
            return 105