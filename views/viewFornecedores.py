from models.fornecedores import *
from models.categoria import *
from controllers.CONfornecedores import *
from controllers.CONcategorias import *
class ViewFornecedores:
    @classmethod
    def add(cls):
        print('Preencha as seguintes informações.\n')
        nome = input('Nome: ')
        cnpj = input('Informe o CNPJ: ')
        categorias = ConCategorias.list()
        for cat in categorias:
            if cat.ativo == True:
                print(f"{cat.serial}- {cat.nome}.")
        cat = input('Informe o numero que representa a categoria:')
        tel = input('Informe o telefone de contato: ')
        aux = ConFornecedores.add(nome, cnpj, cat, tel)
        print(aux)
    @classmethod
    def alter(cls):
        print('Estes são os fornecedores cadastrados:')
        fornecedores = ConFornecedores.list()
        for forn in fornecedores:
            if forn.ativo == True:
                print(f'{forn.id} - {forn.nome}')
        id = int(input('Insira o numero do produto que deseja alterar: '))
        fornecedor: Fornecedores
        for forn in fornecedores:
            if forn.id == id:
                forn = Fornecedores(forn.id, forn.nome, forn.cnpj, forn.categoria,forn.tel, '1')
                break
        aux = input('Deseja alterar o nome?(S/N)').lower()
        if aux == 's':
            forn.nome = input('Nome:')
            aux = 'n'
        aux = input('Deseja alterar o CNPJ?(S/N)').lower()
        if aux == 's':
            forn.cnpj = input('CNPJ: ')
            aux = 'n'
        aux = input('Deseja alterar o telefone?(S/N)').lower()
        if aux == 's':
            forn.tel = input('Telefone: ')
            aux = 'n'
        aux = input('Deseja alterar a categoria?(S/N)').lower()
        if aux == 's':
            cat = ConCategorias.list()
            print('As categorias disponiveis são: ')
            for i in cat:
                if i.ativo == True:
                    print(f'{i.serial} - {i.nome}')
            forn.categoria = input('Qual o numero da nova categoria?')
            aux = 'n'
        aux = ConFornecedores.alter(id, forn)
        print(aux)

    @classmethod
    def delete(cls):
        fornecedores = ConFornecedores.list()
        print('Estes são os fornecedores existentes:\n')
        for forn in fornecedores:
            if forn.ativo == True:
                print(f"{forn.id}- {forn.nome}.")
        id = int(input('Insira o numero do produto que deseja excluir ou 0(zero) para sair?'))
        if id != 0 and id > 0 and id <= len(fornecedores):
            fornecedor: Fornecedores
            for forn in fornecedores:
                if forn.id == id:
                    fornecedor = Fornecedores(forn.id, forn.nome, forn.cnpj, forn.categoria, forn.tel, '1')
                    break
            res = input(f'Tem certeza que deseja excluir o produto?(S/N)').lower()
            if res == 's':
                fornecedor.ativo = False
            aux = ConFornecedores.delete(id, fornecedor)
            print(aux)