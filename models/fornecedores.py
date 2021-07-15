class Fornecedores:
    def __init__(self,nome,cnpj,categoria,telefone):
        self.cnpj = cnpj
        self.nome = nome
        self.categoria = categoria
        self.tel = telefone
        self.ativo = True