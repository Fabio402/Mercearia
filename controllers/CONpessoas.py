from models.pessoas import *
from DAOs.DAOpessoas import *

class ConClientes:
    @classmethod
    def add(cls, nome, cpf, rg, tel, cel, email):
        try:
            pessoas = DaoPessoas.read()
            clientes = DaoCliente.read()
            cliente = Cliente(len(clientes), len(pessoas), nome, cpf, rg, tel, cel, email, '1')
            DaoCliente.save(cliente)
            return 'Cliente salvo!'
        except Exception as e:
            print(e)
    @classmethod
    def list(cls):
        try:
            clientes = DaoCliente.read()
            return clientes
        except Exception as e:
            print(e)
            return 104
    @classmethod
    def alter(cls, id, cliente: Cliente):
            try:
                DaoCliente.alter(id, cliente)
                return "Cliente alterado!"
            except Exception as e:
                print(e)
                return 105
    @classmethod
    def delete(cls, id, cliente: Cliente):
        try:
            DaoCliente.alter(id, cliente)
            return "Cliente deletado!"
        except Exception as e:
            print(e)
            return 105
class ConFuncionarios:
    @classmethod
    def add(cls, nome, cpf, rg, tel, cel, email):
        try:
            pessoas = DaoPessoas.read()
            funcionarios = DaoFuncionario.read()
            funcionario = Funcionario(len(funcionarios), len(pessoas),nome, cpf, rg, tel, cel, email, '1')
            DaoFuncionario.save(funcionario)
            return 'Funcionário salvo!'
        except Exception as e:
            print(e)
    @classmethod
    def list(cls):
        try:
            funcionarios = DaoFuncionario.read()
            return funcionarios
        except Exception as e:
            print(e)
            return 104
    @classmethod
    def alter(cls, id, funcionario: Funcionario):
        try:
            DaoFuncionario.alter(id, funcionario)
            return "Funcionário alterado!"
        except Exception as e:
            print(e)
            return 105
    @classmethod
    def delete(cls, id, funcionario: Funcionario):
        try:
            DaoFuncionario.alter(id, funcionario)
            return "Funcionário deletado!"
        except Exception as e:
            print(e)
            return 105