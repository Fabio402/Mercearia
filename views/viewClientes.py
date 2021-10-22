from models.pessoas import *
from controllers.CONpessoas import *

class ViewClientes:
    @classmethod
    def add(cls):
        print('Preencha as seguintes informações.\n')
        nome = input('Nome:')
        cpf = input('CPF:')
        rg = input('RG:')
        tel = input('Telefone:')
        cel = input('Celular:')
        email = input('E-mail:')
        aux = ConClientes.add(nome, cpf, rg, tel, cel, email)
        print(aux)
    @classmethod
    def alter(cls):
        print('Estes são os clientes cadastrados:')
        clientes = ConClientes.list()
        for cliente in clientes:
            if cliente.ativo == True:
                print(f'{cliente.cliId} - {cliente.nome}')
        id = int(input('Insira o numero do cliente que deseja alterar: '))
        for cli in clientes:
            if cli.cliId == id:
                cliente = Cliente(cli.cliId, cli.pessoaId, cli.nome, cli.cpf, cli.rg, cli.telefone, cli.celular, cli.email, '1')
                break
        aux = input('Deseja alterar o nome?(S/N)').lower()
        if aux == 's':
            cliente.nome = input('Nome:')
            print(cliente.nome)
            aux = 'n'
        aux = input('Deseja alterar o CPF?(S/N)').lower()
        if aux == 's':
            cliente.cpf = input('CPF: ')
            print(cliente.cpf)
            aux = 'n'
        aux = input('Deseja alterar o RG?(S/N)').lower()
        if aux == 's':
            cliente.rg = input('RG: ')
            aux = 'n'
        aux = input('Deseja alterar o Telefone?(S/N)').lower()
        if aux == 's':
            cliente.telefone = input('Telefone: ')
            aux = 'n'
        aux = input('Deseja alterar o celular?(S/N)').lower()
        if aux == 's':
            cliente.celular = input('Celular:')
            aux = 'n'
        aux = input('Deseja alterar o e-mail?(S/N)').lower()
        if aux == 's':
            cliente.email = input('E-mail')
            aux = 'n'
        aux = ConClientes.alter(id, cliente)
        print(aux)

    @classmethod
    def delete(cls):
        print('Estes são os clientes cadastrados:')
        clientes = ConClientes.list()
        for cliente in clientes:
            if cliente.ativo == True:
                print(f'{cliente.cliId} - {cliente.nome}')
        id = int(input('Insira o numero do cliente que deseja excluir: '))
        if id != 0 and id > 0 and id <= len(clientes):
            cliente: Cliente
            for cli in clientes:
                if cli.cliId == id:
                    cliente = Cliente(cli.cliId, cli.pessoaId, cli.nome, cli.cpf, cli.rg, cli.telefone, cli.celular, cli.email, '1')
                    break
            res = input(f'Tem certeza que deseja excluir o cliente?(S/N)').lower()
            if res == 's':
                cliente.ativo = False
            aux = ConClientes.delete(id, cliente)
            print(aux)