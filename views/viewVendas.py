from controllers.CONvendas import *
from controllers.CONpessoas import *
from controllers.CONprodutos import *
from models.vendas import *

class ViewVendas:
    @classmethod
    def add(cls):
        funcionarios = ConFuncionarios.list()
        for func in funcionarios:
            if func.ativo == True:
                print(f"{func.funcId} - {func.nome}.")
        funcId = input('Insira o numero do funcionario: ')
        clientes = ConClientes.list()
        for cli in clientes:
            if cli.ativo == True:
                print(f"{cli.cliId} - {cli.nome}.")
        cliId = input('Insira o numero do cliente: ')
        produtos = ConProdutos.list()
        for prod in produtos:
            if prod.ativo == True:
                print(f"{prod.prodId} - {prod.nome}.")
        op = 'a'
        prodIds = []
        while op != 0:
            op = int(input('Insira o numero de um dos produtos vendidos, ou 0 (zero) para sair: '))
            if op > 0 and op <= len(produtos):
                prodIds.append(op)
        preco = ConVendas.price(prodIds)
        print(f'O preço total da venda é de {preco}')
        aux = input('Deseja dar algum desconto na venda? S/N').lower()
        if aux == 's':
            desconto = float(input('Quanto?'))
        else:
            desconto = 0
        print(f'O preço final da venda é de {float(preco) - float(desconto)}')
        aux = ConVendas.add(funcId, cliId, prodIds, preco, desconto)
        print(aux)
    @classmethod
    def alter(cls):
        vendas = ConVendas.listToday()
        print('As vendas de hoje são: ')
        for venda in vendas:
            if venda.ativo == True:
                print(f"{venda.vendasId}")
        id = input('Insira o numero da venda para alterar: ')
        venda: Vendas
        for vend in vendas:
            if vend.vendasId == id:
                venda = Vendas(id, vend.vendedor, vend.cliente, vend.itemsId, vend.precoTotal, vend.desconto, vend.precoFinal, vend.data, '1')
                break
        aux = input('A venda foi desfeita?(S/N)').lower()
        if aux == 's':
            venda.ativo = False
        aux = input('Deseja alterar o vendedor?(S/N)').lower()
        if aux == 's':
            funcionarios = ConFuncionarios.list()
            for func in funcionarios:
                if func.ativo == True:
                    print(f"{func.funcId} - {func.nome}.")
            venda.vendedor = input('Insira o numero do vendedor: ')
            aux = 'n'
        aux = input('Deseja alterar o cliente?(S/N)').lower()
        if aux == 's':
            clientes = ConClientes.list()
            for cli in clientes:
                if cli.ativo == True:
                    print(f"{cli.cliId} - {cli.nome}.")
            venda.cliente = input('Insira o numero do cliente: ')
            aux = 'n'
        aux = input('Deseja alterar os produtos?(S/N)').lower()
        if aux == 's':
            print(venda.itensId)
            ConVendas.undoEstoque(venda.itensId)
            produtos = ConProdutos.list()
            for prod in produtos:
                if prod.ativo == True:
                    print(f"{prod.prodId} - {prod.nome}.")
            op = 'a'
            prodIds = []
            while op != 0:
                op = int(input('Insira o numero do um dos produtos vendidos, ou 0 (zero) para sair: '))
                if op > 0 and op < len(produtos):
                    prodIds.append(op)
            venda.itensId = prodIds
            aux = 'n'
            preco = ConVendas.price(venda.itensId)
            print(f'O preço total da venda é de {preco}')
        else:
            preco = ConVendas.price(venda.itensId)
        aux = input('Deseja dar algum desconto na venda? S/N').lower()
        if aux == 's':
            desconto = int(input('Quanto?'))
        else:
            desconto = 0
        print(f'O preço final da venda é de {float(preco) - float(desconto)}')
        aux = ConVendas.alter(venda.vendasId, venda)
        print(aux)
