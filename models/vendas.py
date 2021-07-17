class Vendas:
    def __init__(self, id, vendedor, cliente, precoTotal, desconto, precoFinal, ativo, itensId):
        self.vendasId = id
        self.vendedor = vendedor
        self.cliente = cliente
        self.itensId = itensId
        self.precoTotal = precoTotal
        self.desconto = desconto
        self.precoFinal = precoFinal
        self.ativo = ativo
