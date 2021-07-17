class Produto:
    def __init__(self, nome, id, qtd, precoVenda, precoCusto, categoria, *ativo):
        self.nome = nome
        self.prodId = id
        self.qtd = qtd
        self.venda = precoVenda
        self.custo = precoCusto
        self.categoria = categoria
        if len(ativo) == 0:
            self.ativo = True
        else:
            if ativo[0] == '1':
                self.ativo = True
            else:
                self.ativo = False
