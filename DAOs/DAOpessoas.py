from models.pessoas import *

class DaoPessoas:
    @classmethod
    def salvar(cls,id,nome,cpf,rg,telefone,celular,email):
        with open('data/pessoas.txt', 'a') as file:
            file.writelines(id +'|'+ nome +'|'+ cpf +'|'+ rg +'|'+ telefone +'|'+ celular +'|'+ email)

    @classmethod
    def ler(cls):
        with open('data/pessoas.txt', 'r') as file:
            cls.pessoas = file.readlines()
        return cls.pessoas

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('data/funcionarios.txt', 'a') as file:
            file.writelines(funcionario.id + '|' + funcionario.pessoaId + '|' + funcionario.ativo)
            DaoPessoas.salvar(funcionario.pessoaId,funcionario.nome,funcionario.cpf,funcionario.rg,funcionario.telefone,funcionario.celular,funcionario.email)

    @classmethod
    def ler(cls):
        with open('data/funcionarios.txt', 'r') as file:
            cls.funcionarios = file.readlines()
        return cls.funcionarios

class DaoCliente:
    @classmethod
    def salvar(cls, cliente: Cliente):
        with open('data/clientes.txt', 'a') as file:
            file.writelines(cliente.id +'|'+ cliente.pessoaId +'|'+ cliente.ativo)
            DaoPessoas.salvar(cliente.pessoaId, cliente.mome, cliente.cpf, cliente.rg, cliente.telefone, cliente.celular, cliente.email)

    @classmethod
    def ler(cls):
        with open('data/cliente.txt','r') as file:
            cls.clientes = file.readlines()
        return cls.clientes