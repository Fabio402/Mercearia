class DaoCategoria:
    @classmethod
    def save(cls, categoria: Categoria):
        with open('data/categorias.txt','a') as file:
            if categoria.ativo == True:
                categoria.ativo = '1'
            else:
                categoria.ativo = '0'
            file.writelines(str(categoria.serial) +'|'+ categoria.nome +'|'+ categoria.ativo +'\n')

    @classmethod
    def read(cls):
        with open('data/categorias.txt', 'r') as file:
            aux = file.readlines()
            aux = list(map(lambda data: data.replace('\n',''), aux))
            aux = list(map(lambda data: data.split('|'),aux))
            cls.categorias = []
            for i in aux:
                categoria = Categoria(i[1], i[0], i[2])
                cls.categorias.append(categoria)

        return cls.categorias