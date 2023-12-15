from cadastroVacina import CadernetaVacina
class Pessoa:
    __slots__ = ['_email', '_username', '_senha', '_ano', '_cadernetaVacina']

    def __init__(self, email, username, senha, ano):
        self._email = email
        self._username = username
        self._senha = senha
        self._ano =  ano
        self._cadernetaVacina = CadernetaVacina() 

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, NovoEmail):
        self._email = NovoEmail
    @property
    def username(self):
        return self._username
    

