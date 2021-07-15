class venda:
    def __init__(self, id, vendedor, cliente, itensId, precoTotal, desconto, preco):
        self.vendasId = id
        self.vendedor = vendedor
        self.cliente = cliente
        self.itensId = itensId
        self.precoTotal = precoTotal
        self.desconto = desconto
        self.preco = preco
        self.ativo = True
