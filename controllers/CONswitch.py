from controllers.CONprodutos import *
from controllers.CONvendas import *
from controllers.CONpessoas import *
from controllers.CONcategorias import *
from controllers.CONfornecedores import *
from controllers.CONrelatorios import *
class Controller:
    @classmethod
    def switch(cls, opcao):
        try:
            op = int(opcao)
            if op == 1:
                while op2 != 0:
                    op2 = input('1- Produtos\n'
                                '2- Categorias\n'
                                '3- Fornecedores\n'
                                '0- Voltar\n')

                    op3 = input('1- Cadastrar\n'
                                '2- Alterar\n'
                                '3- Remover\n'
                                '0- Voltar\n')

                    if op2 == '1' and op3 == '1':
                        ConProdutos.add()
                    elif op2 == '1' and op3 == '2':
                        ConProdutos.alter()
                    elif op2 == '1' and op3 == '3':
                        ConProdutos.delete()
                    elif op2 == '2' and op3 == '1':
                        ConCategorias.add()
                    elif op2 == '2' and op3 == '2':
                        ConCategorias.alter()
                    elif op2 == '2' and op3 == '3':
                        ConCategorias.delete()
                    elif op2 == '3' and op3 == '1':
                        ConFornecedores.add()
                    elif op2 == '3' and op3 == '2':
                        ConFornecedores.alter()
                    elif op2 == '3' and op3 == '3':
                        ConFornecedores.delete()
                    elif op2 == '0' or op3 == '0':
                        break
                    else:
                        print('Opção inválida\n')

            elif op == 2:
                while op2 != 0:
                    op2 = input('1- Cadastrar\n'
                                '2- Alterar\n'
                                '3- Remover\n'
                                '0- Voltar\n')
                    if op2 == '1':
                        ConVendas.add()
                    elif op2 == '2':
                        ConVendas.alter()
                    elif op2 == '3':
                        ConVendas.delete()
                    elif op2 == '0':
                        continue
                    else:
                        print('Opção inválida!\n')

            elif op == 3:
                while op2 != '0':
                    op2 = input('1- Cadastrar\n'
                                '2- Alterar\n'
                                '3- Remover\n'
                                '0- Voltar\n')
                    if op2 == '1':
                        ConClientes.add()
                    elif op2 == '2':
                        ConClientes.alter()
                    elif op2 == '3':
                        ConClientes.delete()
                    elif op2 == '0':
                        continue
                else:
                    print('Opção inválida!\n')

            elif op == 4:
                while op2 != '0':
                    op2 = input('1- Cadastrar\n'
                                '2- Alterar\n'
                                '3- Remover\n'
                                '0- Voltar\n')
                    if op2 == '1':
                        ConFuncionarios.add()
                    elif op2 == '2':
                        ConFuncionarios.alter()
                    elif op2 == '3':
                        ConFuncionarios.delete()
                    elif op2 == '0':
                        continue
                    else:
                        print('Opção inválida!\n')

            elif op == 5:
                while op2 != '0':
                    op2 = input('1- Relatótio geral de vendas\n'
                                '2- Relatório por data\n'
                                '3- Relatório de produtos mais vendidos\n'
                                '4- Relatório de clientes que mais compram\n'
                                '0- Voltar')
                    if op2 == '1':
                        ConRelatorios.geral()
                    elif op2 == '2':
                        ConRelatorios.data()
                    elif op2 == '3':
                        ConRelatorios.maisVendidos()
                    elif op2 == '4':
                        ConRelatorios.clientes()
                    elif op == '0':
                        continue
                    else:
                        print('Opção inválida!\n')

            elif op == 0:
                print('Até logo')

            else:
                print('Opção inválida! Por favor tente novamente\n')

        except:
            print('Digite um numero inteiro que represente a opção desejada')

