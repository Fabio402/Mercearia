from models.categoria import *
import os
class DaoCategoria:
    @classmethod
    def save(cls, categoria: Categoria):
        with open('../DAOs/data/categorias.txt', 'a') as file:
            if categoria.ativo == True:
                categoria.ativo = '1'
            else:
                categoria.ativo = '0'
            file.writelines(str(categoria.serial) +'|'+ categoria.nome +'|'+ categoria.ativo +'\n')
    @classmethod
    def read(cls):
            with open('../DAOs/data/categorias.txt', 'r') as file:
                aux = file.readlines()
                aux = list(map(lambda data: data.replace('\n', ''), aux))
                aux = list(map(lambda data: data.split('|'),aux))
                cls.categorias = []
                for i in aux:
                    categoria = Categoria(i[1], int(i[0]), i[2])
                    cls.categorias.append(categoria)
                return cls.categorias

    @classmethod
    def alter(cls, alterId, alteracao: Categoria):
        categorias = DaoCategoria.read()
        categoria = list(filter(lambda data: data.serial == alterId, categorias))
        cat = list(map(lambda data: alteracao if (data.serial == alterId) else (data), categorias))
        with open('../DAOs/data/categorias.txt', 'w') as file:
            for i in cat:
                if i.ativo == True:
                    i.ativo = '1'
                else:
                    i.ativo = '0'
                file.writelines(str(i.serial) + '|' + i.nome + '|' + i.ativo + '\n')