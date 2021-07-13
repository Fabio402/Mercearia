class Pessoa:
    def __init__(self,id, nome, cpf, rg, telefone, celular, email):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.celular = celular
        self.email = email
        
class Endereco:
    def __init__(self, id, rua, numero, bairro, cidade, uf):
        self.pessoaId = id
        self.rua = rua
        self.num = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        
class Cliente(Pessoa, Endereco):
    def __init__(self,id, nome, cpf, rg, telefone, celular, emailrua, numero, bairro, cidade, uf):
        self.id
        self.pessoaId
        super(Cliente, self).__init__(id, nome, cpf, rg, telefone, celular, email)
        super(Cliente, self).__init__()
