# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prepesquisa.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_pesquisa(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 14pt \"Constantia\";")
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
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(460, 40, 171, 161))
        self.frame_3.setToolTipDuration(1)
        self.frame_3.setStyleSheet("border-image: url(:/simbolo/logo-_simbolo-removebg-preview.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.botaosair = QtWidgets.QPushButton(self.centralwidget)
        self.botaosair.setGeometry(QtCore.QRect(500, 400, 121, 41))
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
        self.botaovoltar.setGeometry(QtCore.QRect(10, 400, 121, 41))
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
        self.label_principal = QtWidgets.QLabel(self.centralwidget)
        self.label_principal.setGeometry(QtCore.QRect(170, 90, 321, 50))
        self.label_principal.setStyleSheet("\n"
"color: rgb(108, 168, 218);")
        self.label_principal.setObjectName("label_principal")
        self.label_regiao = QtWidgets.QLabel(self.centralwidget)
        self.label_regiao.setGeometry(QtCore.QRect(30, 160, 321, 31))
        self.label_regiao.setObjectName("label_regiao")
        self.label_tempo = QtWidgets.QLabel(self.centralwidget)
        self.label_tempo.setGeometry(QtCore.QRect(30, 200, 201, 31))
        self.label_tempo.setObjectName("label_tempo")
        self.botaopesquisa = QtWidgets.QPushButton(self.centralwidget)
        self.botaopesquisa.setGeometry(QtCore.QRect(230, 350, 211, 41))
        self.botaopesquisa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaopesquisa.setStyleSheet("QPushButton{\n"
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
        self.botaopesquisa.setObjectName("botaopesquisa")
        self.quantsintomas = QtWidgets.QLineEdit(self.centralwidget)
        self.quantsintomas.setGeometry(QtCore.QRect(350, 160, 241, 31))
        self.quantsintomas.setStyleSheet("QLineEdit{\n"
"background-color: rgb(108, 168, 218);\n"
"border-radius:5px;\n"
"}")
        self.quantsintomas.setText("")
        self.quantsintomas.setObjectName("quantsintomas")
        self.quantsintomas_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.quantsintomas_2.setGeometry(QtCore.QRect(190, 200, 261, 81))
        self.quantsintomas_2.setStyleSheet("QLineEdit{\n"
"background-color: rgb(108, 168, 218);\n"
"border-radius:5px;\n"
"}")
        self.quantsintomas_2.setText("")
        self.quantsintomas_2.setObjectName("quantsintomas_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botaosair.setText(_translate("MainWindow", "SAIR"))
        self.botaovoltar.setText(_translate("MainWindow", "VOLTAR"))
        self.label_principal.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Pesquisa de Sintomas!</span></p></body></html>"))
        self.label_regiao.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Quantos Sintomas deseja relatar?</span></p></body></html>"))
        self.label_tempo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Quais sintomas?</span></p></body></html>"))
        self.botaopesquisa.setText(_translate("MainWindow", "Pesquisa Guiada!"))
        self.quantsintomas.setPlaceholderText(_translate("MainWindow", "Ex: 1 ou 2, 3"))
        self.quantsintomas_2.setPlaceholderText(_translate("MainWindow", "Ex: febre, gripe."))
#import simbolo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_pesquisa()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
