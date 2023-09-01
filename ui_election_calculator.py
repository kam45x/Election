# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kalkulator_wyborczy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1176, 858)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(75, 719, 71, 21))
        self.label_3.setPixmap(QPixmap(u"images/Logo_Koalicja_Obywatelska_2023.svg.png"))
        self.label_3.setScaledContents(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(155, 719, 51, 21))
        self.label_5.setPixmap(QPixmap(u"images/Lewica_01.svg.png"))
        self.label_5.setScaledContents(True)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(285, 709, 61, 31))
        self.label_7.setPixmap(QPixmap(u"images/Konfederacja_03.svg.png"))
        self.label_7.setScaledContents(True)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(215, 719, 67, 17))
        self.label_9.setPixmap(QPixmap(u"images/Trzecia_Droga_logo.png"))
        self.label_9.setScaledContents(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(25, 709, 41, 41))
        self.label.setPixmap(QPixmap(u"images/Logo_PiS_Jasne.png"))
        self.label.setScaledContents(True)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 30, 271, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 320, 89, 25))
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 440, 381, 261))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(26, 387, 371, 41))
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(350, 709, 41, 31))
        self.label_14.setPixmap(QPixmap(u"images/Mniejszo\u015b\u0107_Niemiecka.svg.png"))
        self.label_14.setScaledContents(True)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 240, 271, 27))
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.lineEdit_Konfederacja = QLineEdit(self.widget)
        self.lineEdit_Konfederacja.setObjectName(u"lineEdit_Konfederacja")

        self.horizontalLayout_5.addWidget(self.lineEdit_Konfederacja)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(70, 280, 271, 21))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget1)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.textBrowser = QTextBrowser(self.widget1)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_6.addWidget(self.textBrowser)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(71, 80, 271, 27))
        self.horizontalLayout = QHBoxLayout(self.widget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.AutoText)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_PiS = QLineEdit(self.widget2)
        self.lineEdit_PiS.setObjectName(u"lineEdit_PiS")

        self.horizontalLayout.addWidget(self.lineEdit_PiS)

        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(70, 160, 271, 27))
        self.horizontalLayout_3 = QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lineEdit_Lewica = QLineEdit(self.widget3)
        self.lineEdit_Lewica.setObjectName(u"lineEdit_Lewica")

        self.horizontalLayout_3.addWidget(self.lineEdit_Lewica)

        self.widget4 = QWidget(self.centralwidget)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(70, 120, 271, 27))
        self.horizontalLayout_2 = QHBoxLayout(self.widget4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_KO = QLineEdit(self.widget4)
        self.lineEdit_KO.setObjectName(u"lineEdit_KO")

        self.horizontalLayout_2.addWidget(self.lineEdit_KO)

        self.widget5 = QWidget(self.centralwidget)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(71, 201, 271, 27))
        self.horizontalLayout_4 = QHBoxLayout(self.widget5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.lineEdit_TD = QLineEdit(self.widget5)
        self.lineEdit_TD.setObjectName(u"lineEdit_TD")

        self.horizontalLayout_4.addWidget(self.lineEdit_TD)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1176, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kalkulator wyborczy", None))
        self.label_3.setText("")
        self.label_5.setText("")
        self.label_7.setText("")
        self.label_9.setText("")
        self.label.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Wpisz wyniki wybor\u00f3w</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Oblicz", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Podzia\u0142 mandat\u00f3w</span></p></body></html>", None))
        self.label_14.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Konfederacja</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Inne", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#1a5fb4;\">Prawo i Sprawiedliwo\u015b\u0107</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ed333b;\">Nowa Lewica                 </span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ff7800;\">Koalicja Obywatelska    </span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#33d17a;\">Trzecia Droga</span></p></body></html>", None))
    # retranslateUi

