from DAOs.DAOcategoria import *
from models.categoria import *
from views.viewCategorias import *

class ConCategorias:
    @classmethod
    def add(cls):
        while True:
            try:
                serie = 0
                aux = DaoCategoria.read()
                if aux != -1:
                    serie = len(aux)
                    print('Já existe diretório')
                else:
                    serie = 0
                cat = ViewCategorias.add()
                categoria = Categoria(cat, serie, '1')
                DaoCategoria.save(categoria)
            except:
                print('Não foi possivel salvar o sua categoria, tente novamente!')