from models.pessoas import *
import os

class DaoPessoas:
    @classmethod
    def save(cls,id,nome,cpf,rg,telefone,celular,email):
        if os.path.isdir('data/pessoas.txt'):
            with open('data/pessoas.txt', 'a') as file:
                file.writeline(str(id) +'|'+ nome +'|'+ cpf +'|'+ rg +'|'+ telefone +'|'+ celular +'|'+ email)
        else:
            os.makedirs('data/pessoas.txt')
            DaoPessoas.save(id,nome,cpf,rg,telefone,celular,email)

    @classmethod
    def read(cls):
        with open('data/pessoas.txt', 'r') as file:
            aux = file.readlines()
            aux = list(map(lambda data: data.replace('\n', ''), aux))
            cls.pessoas = list(map(lambda data: data.split('|'), aux))

        return cls.pessoas

class DaoFuncionario:
    @classmethod
    def save(cls, funcionario: Funcionario):
        if os.path.isdir('data/funcionarios.txt'):
            with open('data/funcionarios.txt', 'a') as file:
                if funcionario.ativo == True:
                    funcionario.ativo = '1'
                else:
                    funcionario.ativo = '0'
                file.writelines(str(funcionario.funcId) + '|' + str(funcionario.pessoaId) + '|' + funcionario.ativo)
                file.writelines('\n')
                DaoPessoas.save(funcionario.pessoaId, funcionario.nome, funcionario.cpf, funcionario.rg, funcionario.telefone, funcionario.celular, funcionario.email)
        else:
            os.makedirs('data/funcionarios.txt')
            DaoFuncionario.save(funcionario)
    @classmethod
    def read(cls):
        with open('data/funcionarios.txt', 'r') as file:
            aux = file.readlines()
            aux = list(map(lambda data: data.replace('\n',''), aux))
            aux = list(map(lambda data: data.split('|'), aux))
            pessoas = DaoPessoas.read()

            cls.funcionarios = []
            for i in aux:
                for j in pessoas:
                    if(i[1] == j[0]):
                        funcionario = Funcionario(int(i[0]), int(i[1]), j[1], j[2], j[3], j[4], j[5], j[6], i[2])
                        cls.funcionarios.append(funcionario)

        return cls.funcionarios

class DaoCliente:
    @classmethod
    def save(cls, cliente: Cliente):
        if os.path.isdir('data.clientes.txt'):
            with open('data/clientes.txt', 'a') as file:
                if cliente.ativo == True:
                    cliente.ativo = '1'
                else:
                    cliente.ativo = '0'
                file.writelines(str(cliente.cliId) +'|'+ str(cliente.pessoaId) +'|'+ cliente.ativo)
                file.writelines('\n')
                DaoPessoas.save(cliente.pessoaId, cliente.nome, cliente.cpf, cliente.rg, cliente.telefone, cliente.celular, cliente.email)
        else:
            os.makedirs('data/clientes.txt')
            DaoPessoas.save(cliente)

    @classmethod
    def read(cls):
        with open('data/clientes.txt', 'r') as file:
            aux = file.readlines()
            aux = list(map(lambda data: data.replace('\n',''), aux))
            aux = list(map(lambda data: data.split('|'), aux))
            pessoas = DaoPessoas.read()

            cls.clientes = []
            for i in aux:
                for j in pessoas:
                    if(i[1] == j[0]):
                        cliente = Cliente(int(i[0]),int(i[1]), j[1],j[2],j[3],j[4],j[5],j[6],i[2])
                        cls.clientes.append(cliente)
        return cls.clientes