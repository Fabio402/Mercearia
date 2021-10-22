from models.pessoas import *
from controllers.CONpessoas import *

class ViewFuncionarios:
    @classmethod
    def add(cls):
        print('Preencha as seguintes informações.\n')
        nome = input('Nome:')
        cpf = input('CPF:')
        rg = input('RG:')
        tel = input('Telefone:')
        cel = input('Celular:')
        email = input('E-mail:')
        aux = ConFuncionarios.add(nome, cpf, rg, tel, cel, email)
        print(aux)
    @classmethod
    def alter(cls):
        print('Estes são os funcionários cadastrados:')
        funcionarios = ConFuncionarios.list()
        for funcionario in funcionarios:
            if funcionario.ativo == True:
                print(f'{funcionario.funcId} - {funcionario.nome}')
        id = int(input('Insira o numero do funcionário que deseja alterar: '))
        funcionario: Funcionario
        for func in funcionarios:
            if func.funcId == id:
                funcionario = Funcionario(func.funcId, func.pessoaId, func.nome, func.cpf, func.rg, func.telefone, func.celular, func.email, '1')
                break
        aux = input('Deseja alterar o nome?(S/N)').lower()
        if aux == 's':
            funcionario.nome = input('Nome:')
            aux = 'n'
        aux = input('Deseja alterar o CPF?(S/N)').lower()
        if aux == 's':
            funcionario.cpf = input('CPF: ')
            aux = 'n'
        aux = input('Deseja alterar o RG?(S/N)').lower()
        if aux == 's':
            funcionario.rg = input('RG: ')
            aux = 'n'
        aux = input('Deseja alterar o Telefone?(S/N)').lower()
        if aux == 's':
            funcionario.telefone = input('Telefone: ')
            aux = 'n'
        aux = input('Deseja alterar o celular?(S/N)').lower()
        if aux == 's':
            funcionario.celular = input('Celular:')
            aux = 'n'
        aux = input('Deseja alterar o e-mail?(S/N)').lower()
        if aux == 's':
            funcionario.email = input('E-mail:')
            aux = 'n'
        aux = ConFuncionarios.alter(id, funcionario)
        print(aux)
    @classmethod
    def delete(cls):
        print('Estes são os funcionários cadastrados:')
        funcionarios = ConFuncionarios.list()
        for funcionario in funcionarios:
            if funcionario.ativo == True:
                print(f'{funcionario.funcId} - {funcionario.nome}')
        id = int(input('Insira o numero do funcionário que deseja excluir: '))
        if id != 0 and id > 0 and id <= len(funcionarios):
            funcionario: Funcionario
            for func in funcionarios:
                if func.funcId == id:
                    funcionario = Funcionario(func.funcId, func.pessoaId, func.nome, func.cpf, func.rg, func.telefone, func.celular,
                                      func.email, '1')
                    break
            res = input(f'Tem certeza que deseja excluir o funcionário?(S/N)').lower()
            if res == 's':
                funcionario.ativo = False
            aux = ConFuncionarios.delete(id, funcionario)
            print(aux)