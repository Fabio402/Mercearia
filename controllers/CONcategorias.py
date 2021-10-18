from DAOs.DAOcategoria import *
from models.categoria import *

class ConCategorias:
    @classmethod
    def add(cls, nome):
        try:
            aux = DaoCategoria.read()
            categoria = Categoria(nome, len(aux), '1')
            DaoCategoria.save(categoria)
            return 'Cadastro concluido'
        except Exception as e:
            print(e)
    @classmethod
    def list(cls):
        try:
            categorias = DaoCategoria.read()
            return categorias
        except Exception as e:
            print(e)
            return 104
    @classmethod
    def alter(cls, id, cat: Categoria):
        try:
            DaoCategoria.alter(id, cat)
            return "Categoria alterada!"
        except Exception as e:
            print(e)
            return 105
