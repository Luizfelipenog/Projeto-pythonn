# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ideais.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_ideias(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 641, 31))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 181, 198, 255), stop:1 rgba(255, 255, 255, 224));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 450, 641, 31))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(108, 168, 218, 255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_principal = QtWidgets.QLabel(self.centralwidget)
        self.label_principal.setGeometry(QtCore.QRect(250, 60, 181, 51))
        self.label_principal.setStyleSheet("font: 20pt \"Constantia\";\n"
"\n"
"color: rgb(108, 168, 218);")
        self.label_principal.setObjectName("label_principal")
        self.textoideais = QtWidgets.QTextBrowser(self.centralwidget)
        self.textoideais.setGeometry(QtCore.QRect(30, 150, 331, 192))
        self.textoideais.setObjectName("textoideais")
        self.botaosair = QtWidgets.QPushButton(self.centralwidget)
        self.botaosair.setGeometry(QtCore.QRect(10, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botaosair.setFont(font)
        self.botaosair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaosair.setStyleSheet("QPushButton{\n"
"background-color: rgb(72, 187, 198);\n"
"border-radius: 5px;    \n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(72, 187, 198);\n"
"border-radius: 5px;    \n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255 , 255, 255);\n"
"border-radius: 5px;    \n"
"}\n"
"")
        self.botaosair.setObjectName("botaosair")
        self.botaovoltar = QtWidgets.QPushButton(self.centralwidget)
        self.botaovoltar.setGeometry(QtCore.QRect(500, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botaovoltar.setFont(font)
        self.botaovoltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaovoltar.setStyleSheet("QPushButton{\n"
"background-color: rgb(72, 187, 198);\n"
"border-radius: 5px;    \n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(72, 187, 198);\n"
"border-radius: 5px;    \n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255 , 255, 255);\n"
"border-radius: 5px;    \n"
"}\n"
"")
        self.botaovoltar.setObjectName("botaovoltar")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(380, 150, 241, 201))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("logo-versão_completa-removebg-preview.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_principal.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Nossos Ideais!</span></p></body></html>"))
        self.textoideais.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">1. Respeito pela Diversidade:</span><span style=\" font-size:8pt;\"> Reconhecemos a diversidade em todas as suas formas e a valorizamos como um ativo. Estamos empenhados em garantir que todos tenham acesso a serviços de saúde de qualidade, independentemente de sua origem étnica, gênero, orientação sexual, religião ou condição socioeconômica.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2. Transparência e Honestidade:</span><span style=\" font-size:8pt;\"> Promovemos a transparência em todas as nossas operações. Isso significa que compartilhamos informações de forma clara e honesta, permitindo que nossos clientes e colaboradores tomem decisões informadas sobre sua saúde.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">3. Privacidade e Confidencialidade:</span><span style=\" font-size:8pt;\"> Respeitamos a privacidade e a confidencialidade de nossos pacientes e clientes. Todos os dados e informações pessoais são tratados com o mais alto grau de sigilo e segurança.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">4. Empoderamento do Paciente:</span><span style=\" font-size:8pt;\"> Acreditamos que os pacientes devem ser parceiros ativos em suas jornadas de saúde. Encorajamos os pacientes a tomar decisões informadas e a participar ativamente de seu próprio cuidado de saúde.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">5. Acessibilidade:</span><span style=\" font-size:8pt;\"> Estamos comprometidos em tornar os serviços de saúde acessíveis a todos. Buscamos constantemente maneiras de reduzir custos e aumentar a acessibilidade aos tratamentos, exames e informações de saúde.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">6. Responsabilidade Social e Ambiental:</span><span style=\" font-size:8pt;\"> Estamos conscientes de nosso impacto na sociedade e no meio ambiente. Assumimos a responsabilidade de contribuir para o bem-estar da comunidade e para a preservação do meio ambiente.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">7. Aprendizado Contínuo:</span><span style=\" font-size:8pt;\"> Reconhecemos que a área da saúde está em constante evolução. Estamos comprometidos em aprender e aplicar as últimas descobertas e práticas em benefício de nossos pacientes.</span></p></body></html>"))
        self.botaosair.setText(_translate("MainWindow", "SAIR"))
        self.botaovoltar.setText(_translate("MainWindow", "VOLTAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_ideias()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())