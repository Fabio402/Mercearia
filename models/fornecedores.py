class Fornecedores:
    def __init__(self,id,nome,cnpj,categoria,telefone,*ativo):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.categoria = categoria
        self.tel = telefone
        if len(ativo) == 0:
            self.ativo = True
        else:
            if ativo[0] == '1':
                self.ativo = True
            else:
                self.ativo = False