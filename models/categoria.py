class Categoria:
    def __init__(self, nome, serial, *ativo):
        self.nome = nome
        self.serial = serial
        if len(ativo) == 0:
            self.ativo = True
        else:
            if ativo[0] == '1':
                self.ativo = True
            else:
                self.ativo = False


