import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from tela_inicial import Tela_Inicial
from tela_cadastro import Tela_Cadastro
from tela_menu import Tela_Menu
from tela_pesquisa import Tela_pesquisa
from tela_sobrenos import Tela_Sobrenos
from tela_ideias import Tela_ideias
from tela_suporte import Tela_suporte
from tela_vacina import Tela_Vacina
from PyQt5.QtWidgets import QMessageBox
from playwright.sync_api import sync_playwright
import time


from Cliente.cliente import cliente

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow() #Tela inicial 
        self.stack1 = QtWidgets.QMainWindow() #Tela cadastro
        self.stack2 = QtWidgets.QMainWindow() #Tela menu
        self.stack3 = QtWidgets.QMainWindow() #pre pesquisa
        self.stack4 = QtWidgets.QMainWindow() #sobre nos
        self.stack5 = QtWidgets.QMainWindow() #ideias
        self.stack6 = QtWidgets.QMainWindow() #suporte
        self.stack7 = QtWidgets.QMainWindow() #vacina

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_menu = Tela_Menu()
        self.tela_menu.setupUi(self.stack2)
        
        self.tela_pesquisa = Tela_pesquisa()
        self.tela_pesquisa.setupUi(self.stack3)

        self.tela_sobrenos = Tela_Sobrenos()
        self.tela_sobrenos.setupUi(self.stack4)

        self.tela_ideias = Tela_ideias()
        self.tela_ideias.setupUi(self.stack5)

        self.tela_suporte = Tela_suporte()
        self.tela_suporte.setupUi(self.stack6)

        self.tela_vacina = Tela_Vacina()
        self.tela_vacina.setupUi(self.stack7)

        self.QtStack.addWidget(self.stack0) #tela inicial
        self.QtStack.addWidget(self.stack1) #tela cadastro
        self.QtStack.addWidget(self.stack2) #tela menu
        self.QtStack.addWidget(self.stack3) #tela pesquisa
        self.QtStack.addWidget(self.stack4) #tela sobre nos
        self.QtStack.addWidget(self.stack5) #tela ideias
        self.QtStack.addWidget(self.stack6) #tela suporte
        self.QtStack.addWidget(self.stack7) #tela vacina

class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaCadastro) 
        self.tela_inicial.pushButton_2.clicked.connect(self.botaoLogin)
        self.tela_inicial.pushButton_3.clicked.connect(self.botaoSair)

        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastro)
        self.tela_cadastro.pushButton_2.clicked.connect(self.LimparCamposCadastro)
        self.tela_cadastro.pushButton_3.clicked.connect(self.botaoVoltar)

        self.tela_menu.botaovoltar.clicked.connect(self.botaoVoltar)
        self.tela_menu.botaosair.clicked.connect(self.botaoSair)
        self.tela_menu.botaoconsulta.clicked.connect(self.abrirtelaprepesquisa)
        self.tela_menu.botaonos.clicked.connect(self.abrirtelasobrenos)
        self.tela_menu.botaovacina.clicked.connect(self.abrirTelaVacina)
       
        self.tela_pesquisa.botaovoltar.clicked.connect(self.botaoVoltar)
        self.tela_pesquisa.botaosair.clicked.connect(self.botaoSair)
        self.tela_pesquisa.botaopesquisa.clicked.connect(self.executarScriptSintomas)

        self.tela_sobrenos.botaovoltar.clicked.connect(self.botaoVoltar)
        self.tela_sobrenos.botaosair.clicked.connect(self.botaoSair)
        self.tela_sobrenos.botaoideais.clicked.connect(self.abrirtelaideias)
        self.tela_sobrenos.botaosuporte.clicked.connect(self.abrirtelasuporte)

        self.tela_ideias.botaovoltar.clicked.connect(self.botaoVoltar)
        self.tela_ideias.botaosair.clicked.connect(self.botaoSair)

        self.tela_suporte.botaovoltar.clicked.connect(self.botaoVoltar)
        self.tela_suporte.botaosair.clicked.connect(self.botaoSair)

        #Tela Vacina
        self.tela_vacina.toolBox.currentChanged.connect(self.seleciona_page_vacina)
        self.tela_vacina.pushButton_atualizar_infancia.clicked.connect(self.vacinasInfancia)
        self.tela_vacina.pushButton_atualizar_adolescente.clicked.connect(self.vacinasJovem)
        self.tela_vacina.pushButton_atualizar_adulto.clicked.connect(self.vacinasAdulto)
        self.tela_vacina.pushButton_atualizar_idoso.clicked.connect(self.vacinasIdoso)
        self.tela_vacina.pushButton_back.clicked.connect(self.botaoVoltar)
        self.tela_vacina.pushButton_exit.clicked.connect(self.botaoSair)
        
        self.usuario = ""





    def botaoCadastro(self):
        email = self.tela_cadastro.lineEdit.text()
        nome = self.tela_cadastro.lineEdit_2.text()
        senha = self.tela_cadastro.lineEdit_3.text()
        ano = self.tela_cadastro.lineEdit_4.text()
        #cliente(op, email, senha, nome, ano)
        if not(email == '' or nome == '' or senha == '' or ano == ''):
            result = cliente('2', email, senha, nome, ano)
            if result == 'True': 
                QMessageBox.information(None, 'Cadastro de usuario', 'Cadastro Realizado com sucesso!')
                self.QtStack.setCurrentIndex(0)#chama a tela inicial
            else:
                QMessageBox.information(None, 'Cadastro de usuario', 'Usuario já existe, tente outro')
                self.LimparCamposCadastro()
        else:
            QMessageBox.warning(None, 'Cadastro de Usuario', 'Preencha todos os campos!')
        
    def botaoLogin(self):
        email = self.tela_inicial.lineEdit.text()
        senha = self.tela_inicial.lineEdit_2.text()

        if not(email == '' or senha == ''):
            result = cliente('1', email, senha, ' ', ' ')
            self.LimparCamposLogin()
            if result == 'True':#pessoa logada True
                self.QtStack.setCurrentIndex(2)  # Chama a tela de menu
            else:
                QMessageBox.information(None, 'Login', 'Usuario ou Senha incorretos!')

        else:
            QMessageBox.warning(None, 'Login', 'Preencha todos os campos!')
        
    def seleciona_page_vacina(self):
        indice = self.tela_vacina.toolBox.currentIndex()
        if(indice == 0):
            self.tela_vacina.stackedWidget.setCurrentWidget(self.tela_vacina.page_inicio)
        if(indice == 1):
            self.tela_vacina.stackedWidget.setCurrentWidget(self.tela_vacina.page_infancia)
        if(indice == 2):
            self.tela_vacina.stackedWidget.setCurrentWidget(self.tela_vacina.page_adolescente)
        if(indice == 3):
            self.tela_vacina.stackedWidget.setCurrentWidget(self.tela_vacina.page_adulto)
        if(indice == 4):
            self.tela_vacina.stackedWidget.setCurrentWidget(self.tela_vacina.page_idoso)

    def vacinasInfancia(self):
        pass
    def vacinasJovem(self):
        pass
    def vacinasAdulto(self):
        pass
    def vacinasIdoso(self):
        pass
    
    def LimparCamposCadastro(self):
        self.tela_cadastro.lineEdit.setText('')
        self.tela_cadastro.lineEdit_2.setText('')
        self.tela_cadastro.lineEdit_3.setText('')
        self.tela_cadastro.lineEdit_4.setText('')

    def LimparCamposLogin(self):
        self.tela_inicial.lineEdit.setText('')
        self.tela_inicial.lineEdit_2.setText('')

    def botaoVoltar(self):
        indice = self.QtStack.currentIndex()
    
        if indice == 2: #tela de menu
            self.QtStack.setCurrentIndex(0)
        elif indice == 4 or indice == 7:#tela de ideais e de vacina
            self.QtStack.setCurrentIndex(2) #vai pra tela do menu
        elif indice == 6:#tela suporte
            self.QtStack.setCurrentIndex(4)#vai pra tela de sobre nos         
        else:
            self.QtStack.setCurrentIndex(indice - 1)


    def abrirTelaCadastro(self):
        self.LimparCamposCadastro()
        self.QtStack.setCurrentIndex(1)

    def abrirtelaprepesquisa(self):
        self.QtStack.setCurrentIndex(3)

    def abrirtelamenu(self):
        self.QtStack.setCurrentIndex(2)

    def abrirtelasobrenos(self):
        self.QtStack.setCurrentIndex(4)  

    def abrirtelaideias(self):
        self.QtStack.setCurrentIndex(5)

    def abrirtelasuporte(self):
        self.QtStack.setCurrentIndex(6)    

    def abrirTelaVacina(self):
        self.QtStack.setCurrentIndex(7)

    def botaoSair(self):
        exit(0)

    def executarScriptSintomas(self):
        with sync_playwright() as p:
            navegador = p.chromium.launch(headless=True)
            pagina = navegador.new_page()
            pagina.goto("https://analisesintomas.com")

            sintomas_str = self.tela_pesquisa.quantsintomas.text()
            sintomas = self.obterListaSintomas(sintomas_str)

            for sintoma_nome in sintomas:
                self.sintomas(pagina, sintoma_nome)

            pagina.locator('xpath=//*[@id="message_send"]').click()

            # Imprimir o XPath fornecido
            mensagem_xpath = '//*[@id="divResultadoDoencasDir"]/span[1]'
            mensagem_elemento = pagina.locator(mensagem_xpath)
            mensagem_texto = mensagem_elemento.inner_text()

            mensagem_probabilidade_xpath = '//*[@id="divResultadoDoencasDir"]/span[2]'
            mensagem_elemento2 = pagina.locator(mensagem_probabilidade_xpath)
            mensagem_texto2 = mensagem_elemento2.inner_text()

            mensagem_completa = f'A possível doença: {mensagem_texto}\nProbabilidade: {mensagem_texto2}'

            QMessageBox.warning(None, 'Resultado da Análise de Sintomas', mensagem_completa)



            # Aguardar um tempo para observar a interação (opcional)
            #time.sleep(5)

    def obterListaSintomas(self, sintomas_str):
        lista_sintomas = sintomas_str.split(',')
        return lista_sintomas

    def sintomas(self, pagina, sintoma_nome):
        pagina.locator('xpath=//*[@id="sintomaPesquisa"]').click()
        pagina.fill('xpath=//*[@id="sintomaPesquisa"]', sintoma_nome)
        pagina.locator('xpath=//*[@id="btPesquisaSintoma"]').click()
        self.clicar(pagina)

    def clicar(self, pagina):
        elementos = pagina.locator('//td[contains(@class, "tdAzulClaro")][contains(@onclick, "adicionarSintomaLista")]')

        if elementos.count() > 0:
            primeiro_elemento = elementos.first
            primeiro_elemento.hover()
            #time.sleep(1)
            primeiro_elemento.click()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
