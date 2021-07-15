class Pessoa:
    def __init__(self, id, nome, cpf, rg, telefone, celular, email):
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
        self.ativo = True

class Cliente(Pessoa):
    def __init__(self, cliId, pessoaId, nome, cpf, rg, telefone, celular, email):
        self.id = cliId
        self.pessoaId = pessoaId
        self.ativo = True
        super(Cliente, self).__init__(pessoaId, nome, cpf, rg, telefone, celular, email)

class Funcionario(Pessoa):
    def __init__(self, funcId, pessoaId, nome, cpf, rg, telefone, celular, email):
        self.id = funcId
        self.pessoaId = pessoaId
        self.ativo = True
        super(Funcionario, self).__init__(pessoaId, nome, cpf, rg, telefone, celular, email)
