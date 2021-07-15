from models.categoria import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria: Categoria):
        with open('data/categorias.txt','a') as file:
            file.writelines(categoria.serial +'|'+categoria.nome +'|'+ categoria.ativo)

    @classmethod
    def ler(cls, categorias: Categoria):
        with open('data/categorias.txt', 'r') as file:
            cls.categorias = file.readlines()
        return cls.categorias