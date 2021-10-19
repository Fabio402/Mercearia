from controllers.CONcategorias import *
class ViewCategorias:
    @classmethod
    def add(cls):
        nome = input('Insira o nome da nova categoria: ')
        aux = ConCategorias.add(nome)
        print(aux)
    @classmethod
    def alter(cls):
        categorias = ConCategorias.list()
        print('Estas são as categorias existentes:\n')
        for cat in categorias:
            if cat.ativo == True:
                print(f"{cat.serial}- {cat.nome}.")
        id = int(input('Insira o numero da categoria deseja editar ou 0(zero) para sair?'))
        if id != 0 and id > 0 and id <= len(categorias):
            categoria = Categoria('a',id,'1')
            for cat in categorias:
                if cat.serial == id:
                    categoria.nome = cat.nome
            res = input('alterar o nome?(S/N)').lower()
            if res == 's':
                categoria.nome = input('Qual o novo nome?')
            aux = ConCategorias.alter(id, categoria)
            print(aux)
    @classmethod
    def delete(cls):
        categorias = ConCategorias.list()
        print('Estas são as categorias existentes:\n')
        for cat in categorias:
            if cat.ativo == True:
                print(f"{cat.serial}- {cat.nome}.")
        id = int(input('Insira o numero da categoria deseja excluir ou 0(zero) para sair?'))
        if id != 0 and id > 0 and id <= len(categorias):
            categoria = Categoria('a', id, '1')
            for cat in categorias:
                if cat.serial == id:
                    categoria.nome = cat.nome
            res = input(f'Tem certeza que deseja excluir a categoria?(S/N)').lower()
            if res == 's':
                categoria.ativo = False
            aux = ConCategorias.delete(id, categoria)
            print(aux)