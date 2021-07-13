class Categoria:
    def __init__(self, nome, last):
        self.nome = nome
        self.serial = last+1


class Produto:
    def __init__(self, nome, last, qtd, precoVenda, precoCusto):
        self.nome = nome
        self.serial = last+1