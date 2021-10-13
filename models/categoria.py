class Categoria:
    def __init__(self, nome, serial, *ativo):
        self.nome = nome
        self.serial = serial
        if ativo == True:
            self.ativo = True
        else:
            if ativo[0] == '1':
                self.ativo = True
            else:
                self.ativo = False
