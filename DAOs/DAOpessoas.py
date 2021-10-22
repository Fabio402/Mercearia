from models.pessoas import *

class DaoPessoas:
    @classmethod
    def save(cls, id, nome, cpf, rg, telefone, celular, email):
            with open('../DAOs/data/pessoas.txt', 'a') as file:
                file.writelines(str(id) +'|'+ nome +'|'+ cpf +'|'+ rg +'|'+ telefone +'|'+ celular +'|'+ email+'\n')
    @classmethod
    def read(cls):
        with open('../DAOs/data/pessoas.txt', 'r') as file:
            aux = file.readlines()
            aux = list(map(lambda data: data.replace('\n', ''), aux))
            aux = list(map(lambda data: data.split('|'), aux))
            cls.pessoas = []
            for i in aux:
                pessoa = Pessoa(int(i[0]), i[1], i[2], i[3], i[4], i[5], i[6])
                cls.pessoas.append(pessoa)
        return cls.pessoas
    @classmethod
    def alter(cls, alterId, nome, cpf, rg, telefone, celular, email ):
        pessoa = Pessoa(alterId,nome,cpf,rg,telefone,celular,email)
        pessoas = DaoPessoas.read()
        pess = list(map(lambda data: pessoa if (int(data.id) == alterId) else (data), pessoas))
        with open('../DAOs/data/pessoas.txt', 'w') as file:
            for i in pess:
                file.writelines(str(i.id) +'|'+ i.nome +'|'+ i.cpf +'|'+ i.rg +'|'+ i.telefone +'|'+ i.celular +'|'+ i.email + '\n')
class DaoFuncionario:
    @classmethod
    def save(cls, funcionario: Funcionario):
            with open('../DAOs/data/funcionarios.txt', 'a') as file:
                if funcionario.ativo == True:
                    funcionario.ativo = '1'
                else:
                    funcionario.ativo = '0'
                file.writelines(str(funcionario.funcId) + '|' + str(funcionario.pessoaId) + '|' + funcionario.ativo + '\n')
                DaoPessoas.save(funcionario.pessoaId, funcionario.nome, funcionario.cpf, funcionario.rg, funcionario.telefone, funcionario.celular, funcionario.email)
    @classmethod
    def read(cls):
        with open('../DAOs/data/funcionarios.txt', 'r') as file:
            aux = file.readlines()
            aux = list(map(lambda data: data.replace('\n',''), aux))
            aux = list(map(lambda data: data.split('|'), aux))
            pessoas = DaoPessoas.read()
            cls.funcionarios = []
            for i in aux:
                for j in pessoas:
                    if int(i[1]) == int(j.id):
                        funcionario = Funcionario(int(i[0]), j.id, j.nome, j.cpf, j.rg, j.telefone, j.celular, j.email, i[2])
                        cls.funcionarios.append(funcionario)
            return cls.funcionarios
    @classmethod
    def alter(cls,alterId, funcionario: Funcionario):
        funcionarios = DaoFuncionario.read()
        func = list(map(lambda data: funcionario if (data.funcId == alterId) else (data), funcionarios))
        DaoPessoas.alter(funcionario.pessoaId, funcionario.nome, funcionario.cpf, funcionario.rg, funcionario.telefone,
                         funcionario.celular, funcionario.email)
        with open('../DAOs/data/clientes.txt', 'w') as file:
            for i in func:
                if i.ativo == True:
                    i.ativo = '1'
                else:
                    i.ativo = '0'
                file.writelines(str(i.funcId) + '|' + str(i.pessoaId) + '|' + i.ativo + '\n')
class DaoCliente:
    @classmethod
    def save(cls, cliente: Cliente):
        with open('../DAOs/data/clientes.txt', 'a') as file:
            if cliente.ativo == True:
                cliente.ativo = '1'
            else:
                cliente.ativo = '0'
            file.writelines(str(cliente.cliId) +'|'+ str(cliente.pessoaId) +'|'+ cliente.ativo+ '\n')
            DaoPessoas.save(cliente.pessoaId, cliente.nome, cliente.cpf, cliente.rg, cliente.telefone, cliente.celular, cliente.email)
    @classmethod
    def read(cls):
        with open('../DAOs/data/clientes.txt', 'r') as file:
            aux = file.readlines()
            aux = list(map(lambda data: data.replace('\n',''), aux))
            aux = list(map(lambda data: data.split('|'), aux))
            pessoas = DaoPessoas.read()
            cls.clientes = []
            for i in aux:
                for j in pessoas:
                    if int(i[1]) == int(j.id):
                        cliente = Cliente(int(i[0]), j.id, j.nome, j.cpf, j.rg, j.telefone, j.celular, j.email, i[2])
                        cls.clientes.append(cliente)
            return cls.clientes
    @classmethod
    def alter(cls, alterId, cliente: Cliente):
        clientes = DaoCliente.read()
        cli = list(map(lambda data: cliente if (data.cliId == alterId) else (data), clientes))
        DaoPessoas.alter(cliente.pessoaId, cliente.nome, cliente.cpf, cliente.rg, cliente.telefone,
                         cliente.celular, cliente.email)
        with open('../DAOs/data/clientes.txt', 'w') as file:
            for i in cli:
                if i.ativo == True:
                    i.ativo = '1'
                else:
                    i.ativo = '0'
                file.writelines(str(i.cliId) +'|'+ str(i.pessoaId) +'|'+ i.ativo + '\n')