from controllers.CONrelatorios import *
class ViewRelatorios:
    @classmethod
    def geral(cls):
        print('Relatório geral de estoque:')
        rel = ConRelatorios.geral()
        print('ID - Produto - Quantidade')
        for i in rel:
            print(f'{i[0]} - {i[1]} - {i[2]}')
    @classmethod
    def data(cls):
        print('Relatório de vendas por data:')
        data = input('Quer ver as vendas de que dia? (AAAA-MM-DD)')
        rel = ConRelatorios.data(data)
        if len(rel) != 0:
            print('venda - valor')
            for i in rel:
                print(f'{i[0]} - {i[1]}')
        else:
            print('Nenhuma venda foi encontrada!' \
                   'Verifique o formato da data informado,' \
                   'ele deve estar como ano/mes/dia.')
    @classmethod
    def maisVendidos(cls):
        print('Relatório de produtos mais vendidos')
        rel = ConRelatorios.maisVendidos()
        print('quantidade vendida - produto')
        for i in rel:
            print(f'{i[0]} - {i[1]}')
    @classmethod
    def clientes(cls):
        print('Relatório de clientes que mais compram')
        rel = ConRelatorios.clientes()
        print('cliente - valor comprado')
        for i in rel:
            print(f'{i[0]} - {i[1]}')