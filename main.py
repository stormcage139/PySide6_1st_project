from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from app2 import Ui_MainWindow
from datetime import datetime



class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.add_event.clicked.connect(self.add_new_event)
        self.remove_event.clicked.connect(self.remove_old_event)
        self.listView.

    def add_new_event(self):
        a = self.lineEdit.text()
        with open("todo_list.txt", "a", encoding="utf-8") as file:
            file.write(a + "\n")

    def remove_old_event(self):
        print("removed")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec())
