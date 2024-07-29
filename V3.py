# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'V2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListView,
                               QMainWindow, QPushButton, QSizePolicy, QWidget, QListWidget)
from PySide6 import QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 924)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(430, 740, 221, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_event = QPushButton(self.layoutWidget)
        self.add_event.setObjectName(u"add_event")

        self.horizontalLayout.addWidget(self.add_event, 0, Qt.AlignmentFlag.AlignHCenter)

        self.remove_event = QPushButton(self.layoutWidget)
        self.remove_event.setObjectName(u"remove_event")

        self.horizontalLayout.addWidget(self.remove_event, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(290, 680, 511, 61))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(-5, 1, 1081, 681))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"to_do_list", None))
        self.add_event.setText(QCoreApplication.translate("MainWindow",
                                                          u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u0435",
                                                          None))
        self.remove_event.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u0435",
                                                                 None))
        # retranslateUi

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
