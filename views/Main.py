from views.viewProdutos import *
from controllers.CONprodutos import *
from views.viewCategorias import *
from views.viewFornecedores import *
from views.viewClientes import *
from views.viewFuncionarios import *
from views.viewVendas import *

def main():
    op = 10
    while (op != '0'):
        op = int(input('Escolha uma opção de uso do sistema:\n'
                        '1- Produtos\n'
                        '2- Vendas\n'
                        '3- Gerenciamento de clientes\n'
                        '4- Gerenciamento de funcionários\n'
                        '5- Relatórios\n'
                        '0- Sair\n'))
        if op == 1:
            op2 = 10
            while op2 != 0:
                op2 = int(input('1- Produtos\n'
                        '2- Categorias\n'
                        '3- Fornecedores\n'
                        '0- Voltar\n'))
                op3 = int(input('1- Cadastrar\n'
                        '2- Alterar\n'
                        '3- Remover\n'
                        '0- Voltar\n'))
                if op2 == 1 and op3 == 1:
                    ViewProdutos.add()
                elif op2 == 1 and op3 == 2:
                    ViewProdutos.alter()
                elif op2 == 1 and op3 == 3:
                    ViewProdutos.delete()
                elif op2 == 2 and op3 == 1:
                    ViewCategorias.add()
                elif op2 == 2 and op3 == 2:
                    ViewCategorias.alter()
                elif op2 == 2 and op3 == 3:
                    ViewCategorias.delete()
                elif op2 == 3 and op3 == 1:
                    ViewFornecedores.add()
                elif op2 == 3 and op3 == 2:
                    ViewFornecedores.alter()
                elif op2 == 3 and op3 == 3:
                    ViewFornecedores.delete()
                elif op2 == 0 or op3 == 0:
                        continue
                else:
                    print('Opção inválida\n')
        elif op == 2:
            op2 = 0
            while op2 != 0:
                op2 = int(input('1- Cadastrar\n'
                    '2- Alterar\n'
                    '3- Remover\n'
                    '0- Voltar\n'))
                if op2 == '1':
                    ViewVendas.add()
                elif op2 == '2':
                    ViewVendas.alter()
                elif op2 == '3':
                    ViewVendas.delete()
                elif op2 == 0:
                    continue
                else:
                    print('Opção inválida!\n')
        elif op == 3:
            op2 = 10
            while op2 != 0:
                op2 = int(input('1- Cadastrar\n'
                    '2- Alterar\n'
                    '3- Remover\n'
                    '0- Voltar\n'))
                if op2 == 1:
                    ViewClientes.add()
                elif op2 == 2:
                    ViewClientes.alter()
                elif op2 == 3:
                    ViewClientes.delete()
                elif op2 == 0:
                    continue
                else:
                    print('Opção inválida!\n')
        elif op == 4:
            op2 = 10
            while op2 != 0:
                op2 = int(input('1- Cadastrar\n'
                    '2- Alterar\n'
                    '3- Remover\n'
                    '0- Voltar\n'))
                if op2 == 1:
                    ViewFuncionarios.add()
                elif op2 == 2:
                    ViewFuncionarios.alter()
                elif op2 == 3:
                    ViewFuncionarios.delete()
                elif op2 == 0:
                    continue
                else:
                    print('Opção inválida!\n')
        elif op == 5:
            op2 = 10
            while op2 != 0:
                op2 = int(input('1- Relatótio geral de vendas\n'
                    '2- Relatório por data\n'
                    '3- Relatório de produtos mais vendidos\n'
                    '4- Relatório de clientes que mais compram\n'
                    '0- Voltar'))
                if op2 == '1':
                    ViewRelatorios.geral()
                elif op2 == '2':
                    ViewRelatorios.data()
                elif op2 == '3':
                    ViewRelatorios.maisVendidos()
                elif op2 == '4':
                    ViewRelatorios.clientes()
                elif op == 0:
                    continue
                else:
                    print('Opção inválida!\n')
        elif op == 0:
            break
        else:
            print('Opção inválida! Por favor tente novamente\n')

if __name__ == '__main__':
    main()