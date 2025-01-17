# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App/casino.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
# import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_kabinet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kabinet.setGeometry(QtCore.QRect(0, 0, 200, 50))
        self.btn_kabinet.setObjectName("btn_kabinet")
        self.btn_coinflip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_coinflip.setGeometry(QtCore.QRect(200, 0, 200, 50))
        self.btn_coinflip.setObjectName("btn_coinflip")
        self.btn_crash = QtWidgets.QPushButton(self.centralwidget)
        self.btn_crash.setGeometry(QtCore.QRect(400, 0, 200, 50))
        self.btn_crash.setObjectName("btn_crash")
        self.btn_mines = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mines.setGeometry(QtCore.QRect(600, 0, 200, 50))
        self.btn_mines.setObjectName("btn_mines")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 50, 800, 750))
        self.stackedWidget.setObjectName("stackedWidget")
        self.kabinet_page = QtWidgets.QWidget()
        self.kabinet_page.setObjectName("kabinet_page")
        self.bal_label = QtWidgets.QLabel(self.kabinet_page)
        self.bal_label.setGeometry(QtCore.QRect(180, 40, 450, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bal_label.setFont(font)
        self.bal_label.setObjectName("bal_label")
        self.maxbal_label = QtWidgets.QLabel(self.kabinet_page)
        self.maxbal_label.setGeometry(QtCore.QRect(180, 220, 450, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maxbal_label.setFont(font)
        self.maxbal_label.setObjectName("maxbal_label")
        self.maxwinstreak_coinflip = QtWidgets.QLabel(self.kabinet_page)
        self.maxwinstreak_coinflip.setGeometry(QtCore.QRect(180, 320, 451, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maxwinstreak_coinflip.setFont(font)
        self.maxwinstreak_coinflip.setObjectName("maxwinstreak_coinflip")
        self.maxwinstreak_crash = QtWidgets.QLabel(self.kabinet_page)
        self.maxwinstreak_crash.setGeometry(QtCore.QRect(180, 410, 451, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maxwinstreak_crash.setFont(font)
        self.maxwinstreak_crash.setObjectName("maxwinstreak_crash")
        self.maxwinstreak_mines = QtWidgets.QLabel(self.kabinet_page)
        self.maxwinstreak_mines.setGeometry(QtCore.QRect(180, 480, 451, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maxwinstreak_mines.setFont(font)
        self.maxwinstreak_mines.setObjectName("maxwinstreak_mines")
        self.popolnenye_lineedit = QtWidgets.QLineEdit(self.kabinet_page)
        self.popolnenye_lineedit.setGeometry(QtCore.QRect(670, 720, 113, 22))
        self.popolnenye_lineedit.setObjectName("popolnenye_lineedit")
        self.popolnenye_btn = QtWidgets.QPushButton(self.kabinet_page)
        self.popolnenye_btn.setGeometry(QtCore.QRect(520, 710, 141, 28))
        self.popolnenye_btn.setObjectName("popolnenye_btn")
        self.stackedWidget.addWidget(self.kabinet_page)
        self.coinflip_page = QtWidgets.QWidget()
        self.coinflip_page.setObjectName("coinflip_page")
        self.coinflip_gif = QtWidgets.QLabel(self.coinflip_page)
        self.coinflip_gif.setGeometry(QtCore.QRect(60, 20, 191, 211))
        self.coinflip_gif.setObjectName("coinflip_gif")
        self.coinflip_greencoin_img = QPixmap("C:/Users/Roma/PycharmProjects/OlymTasks/App/Coingreen_cr.png")
        self.coinflip_redcoin_img = QPixmap("C:/Users/Roma/PycharmProjects/OlymTasks/App/Coinred_cr.png")

        self.yourbet_coinflip_lineedit = QtWidgets.QLineEdit(self.coinflip_page)
        self.yourbet_coinflip_lineedit.setGeometry(QtCore.QRect(390, 250, 241, 41))
        self.yourbet_coinflip_lineedit.setObjectName("yourbet_coinflip_lineedit")
        self.yourbet_coinflip = QtWidgets.QLabel(self.coinflip_page)
        self.yourbet_coinflip.setGeometry(QtCore.QRect(390, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yourbet_coinflip.setFont(font)
        self.yourbet_coinflip.setObjectName("yourbet_coinflip")
        self.headortail_label = QtWidgets.QLabel(self.coinflip_page)
        self.headortail_label.setGeometry(QtCore.QRect(60, 250, 201, 41))
        self.headortail_label.setObjectName("headortail_label")
        self.yourbal_coinflip = QtWidgets.QLabel(self.coinflip_page)
        self.yourbal_coinflip.setGeometry(QtCore.QRect(420, 40, 341, 41))
        self.yourbal_coinflip.setObjectName("yourbal_coinflip")
        self.btn_flipcoin = QtWidgets.QPushButton(self.coinflip_page)
        self.btn_flipcoin.setGeometry(QtCore.QRect(640, 250, 141, 41))
        self.btn_flipcoin.setObjectName("btn_flipcoin")
        self.martingale_checkbox = QtWidgets.QCheckBox(self.coinflip_page)
        self.martingale_checkbox.setGeometry(QtCore.QRect(390, 310, 111, 30))
        self.martingale_checkbox.setObjectName("martingale_checkbox")
        self.constantbet_lineedit = QtWidgets.QLineEdit(self.coinflip_page)
        self.constantbet_lineedit.setGeometry(QtCore.QRect(510, 317, 113, 22))
        self.constantbet_lineedit.setObjectName("lineEdit")
        self.automartingale_checkbox = QtWidgets.QCheckBox(self.coinflip_page)
        self.automartingale_checkbox.setGeometry(QtCore.QRect(660, 310, 121, 30))
        self.automartingale_checkbox.setObjectName("automartingale_checkbox")
        self.stackedWidget.addWidget(self.coinflip_page)
        self.crash_page = QtWidgets.QWidget()
        self.crash_page.setObjectName("crash_page")
        self.stackedWidget.addWidget(self.crash_page)
        self.zapusk = QtWidgets.QPushButton(self.crash_page)
        self.zapusk.setGeometry(QtCore.QRect(100, 100, 221, 211))
        self.zapusk.setObjectName("zapusk")

        self.mines_page = QtWidgets.QWidget()
        self.mines_page.setObjectName("mines_page")
        self.label = QtWidgets.QLabel(self.mines_page)
        self.label.setGeometry(QtCore.QRect(300, 250, 221, 211))
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Roma/PycharmProjects/OlymTasks/App/Dog.jpg"))
        self.label.resize(QtGui.QPixmap("C:/Users/Roma/PycharmProjects/OlymTasks/App/Dog.jpg").width(), QtGui.QPixmap("C:/Users/Roma/PycharmProjects/OlymTasks/App/Dog.jpg").height())
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.mines_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Casino"))
        self.btn_kabinet.setText(_translate("MainWindow", "Личный Кабинет"))
        self.btn_coinflip.setText(_translate("MainWindow", "Coinflip"))
        self.btn_crash.setText(_translate("MainWindow", "Crash"))
        self.btn_mines.setText(_translate("MainWindow", "Mines"))
        self.bal_label.setText(_translate("MainWindow", "TextLabel"))
        self.maxbal_label.setText(_translate("MainWindow", "TextLabel"))
        self.maxwinstreak_coinflip.setText(_translate("MainWindow", "TextLabel"))
        self.maxwinstreak_crash.setText(_translate("MainWindow", "TextLabel"))
        self.maxwinstreak_mines.setText(_translate("MainWindow", "TextLabel"))
        self.popolnenye_btn.setText(_translate("MainWindow", "Пополнить баланс"))
        # self.coinflip_gif.setText(_translate("MainWindow", "ТУТ БУДЕТ ГИФКА"))
        self.yourbet_coinflip.setText(_translate("MainWindow", "Введите ставку:"))
        self.headortail_label.setText(_translate("MainWindow", "тут результат броска"))
        self.yourbal_coinflip.setText(_translate("MainWindow", "ТУТ ДОЛЖЕН БЫТЬ БАЛАНС"))
        self.btn_flipcoin.setText(_translate("MainWindow", "Подбросить монетку"))
        self.martingale_checkbox.setText(_translate("MainWindow", "MartinGale"))
        self.automartingale_checkbox.setText(_translate("MainWindow", "AutoMartinGale"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
