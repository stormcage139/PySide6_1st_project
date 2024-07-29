from casino import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, QRect
import sys, random, threading, time


class CrashGame(QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.value = 0

    def run(self):
        # self.mainwindow.zapusk.hide()
        value = 0
        while value <= 100:
            self.mainwindow.progress.setValue(value)
            # time.sleep(0.3)
            value += 1
        # time.sleep(1)
        # self.mainwindow.zapusk.show()


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_kabinet.clicked.connect(self.swap_pages)
        self.btn_coinflip.clicked.connect(self.swap_pages)
        self.btn_crash.clicked.connect(self.swap_pages)
        self.btn_mines.clicked.connect(self.swap_pages)
        self.bal = 0
        self.yourbal_coinflip.setText(f"Баланс: {self.bal}")
        self.popolnenye_btn.clicked.connect(self.popolnenye)
        self.bal_label.setText(f"Баланс: {self.bal}")
        self.btn_flipcoin.clicked.connect(self.flipcoin)
        self.constantbet = 1
        self.bet = 0
        self.zapusk.clicked.connect(self.startcrash)

        self.progressbar_instance = CrashGame(mainwindow=self)




        self.progress = QtWidgets.QProgressBar(self.crash_page)
        self.progress.setGeometry(QtCore.QRect(300, 250, 221, 211))
        self.progress.setObjectName("progress")

    def startcrash(self):
        self.progressbar_instance.start()


    def flipcoin(self):
        if self.automartingale_checkbox.isChecked():
            if not self.constantbet_lineedit.text():
                return 0
            self.constantbet = int(self.constantbet_lineedit.text())
            self.bet = self.constantbet
            self.startbal = self.bal
            for i in range(10000):
                if self.bet > self.bal:
                    break
                if random.randint(0, 1) == 1:
                    self.bal += self.bet
                    self.bet = self.constantbet
                else:
                    self.bal -= self.bet
                    self.bet *= 2
            if self.bal < self.startbal:
                self.headortail_label.setText(f"Вы проиграли: {self.startbal - self.bal}")
            else:
                self.headortail_label.setText(f"Вы выиграли: {self.bal - self.startbal}")
            self.yourbal_coinflip.setText(f"Баланс: {self.bal}")

        elif self.martingale_checkbox.isChecked():
            if not self.constantbet_lineedit.text():
                return 0
            self.constantbet = int(self.constantbet_lineedit.text())
            if self.yourbet_coinflip_lineedit.text():
                self.bet = int(self.yourbet_coinflip_lineedit.text())
            else:
                self.bet = 0
            if self.bet < self.constantbet:
                self.bet = self.constantbet
            if random.randint(0, 1) == 1:
                self.bal += self.bet
                self.headortail_label.setText(f"Вы выиграли: {self.bet * 2}")
                self.bet = self.constantbet
                self.coinflip_gif.setPixmap(self.coinflip_greencoin_img)
            else:
                self.bal -= self.bet
                self.headortail_label.setText(f"Вы проиграли: {self.bet}")
                self.bet *= 2
                self.coinflip_gif.setPixmap(self.coinflip_redcoin_img)
            self.yourbet_coinflip_lineedit.setText(f"{self.bet}")
            self.coinflip_gif.resize(200, 200)
        else:
            if self.yourbet_coinflip_lineedit.text():
                self.bet = int(self.yourbet_coinflip_lineedit.text())
            else:
                return 0
            if random.randint(0, 1) == 1:
                self.bal += self.bet
                self.headortail_label.setText(f"Вы выиграли: {self.bet * 2}")
                self.coinflip_gif.setPixmap(self.coinflip_greencoin_img)
            else:
                self.headortail_label.setText(f"Вы проиграли: {self.bet}")
                self.bal -= self.bet
                self.coinflip_gif.setPixmap(self.coinflip_redcoin_img)
        self.coinflip_gif.resize(200, 200)
        self.yourbal_coinflip.setText(f"Баланс: {self.bal}")

    def popolnenye(self):
        self.bal += int(self.popolnenye_lineedit.text())
        self.bal_label.setText(f"Баланс: {self.bal}")

    def swap_pages(self):
        if self.sender() == self.btn_kabinet:
            self.stackedWidget.setCurrentIndex(0)
        elif self.sender() == self.btn_coinflip:
            self.stackedWidget.setCurrentIndex(1)
        elif self.sender() == self.btn_crash:
            self.stackedWidget.setCurrentIndex(2)
        elif self.sender() == self.btn_mines:
            self.stackedWidget.setCurrentIndex(3)
        self.yourbal_coinflip.setText(f"Баланс: {self.bal}")
        self.bal_label.setText(f"Баланс: {self.bal}")
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# обвязка для запуска
app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec_())