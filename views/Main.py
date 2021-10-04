from controllers.CONswitch import *

op = 0
while(op != '0'):
    op = int(input('Escolha uma opção de uso do sistema:\n'
          '1- Produtos\n'
          '2- Vendas\n'
          '3- Gerenciamento de clientes\n'
          '4- Gerenciamento de funcionários\n'
          '5- Relatórios\n'
          '0- Sair\n'))
    Controller.switch(op)


