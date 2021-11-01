class Vendas:
    def __init__(self, id, vendedor, cliente, itensId, precoTotal, desconto, precoFinal,data, ativo):
        self.vendasId = id
        self.vendedor = vendedor
        self.cliente = cliente
        self.itensId = itensId
        self.precoTotal = precoTotal
        self.desconto = desconto
        self.precoFinal = precoFinal
        self.data = data
        if ativo == True:
            self.ativo = True
        else:
            if ativo[0] == '1':
                self.ativo = True
            else:
                self.ativo = False
