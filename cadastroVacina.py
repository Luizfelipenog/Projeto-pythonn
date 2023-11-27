class CadernetaVacina:

    def __init__(self):
        self._vacinado = []
        self._reforco = {} #dt ano, influenza mes
    
    def cadastraVacina(self, vacina):
        if not(self.buscaVacina(vacina)):
            self._vacinado.append(vacina)

    def buscaVacina(self, vacina):
        for v in self._vacinado:
            if(v == vacina):
                return True
            else:
                return False

    def cadastraReforco(self, reforco, ano):
        self._reforco[reforco] = ano

        





    
