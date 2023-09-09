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
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 858)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(630, 290, 71, 21))
        self.label_3.setPixmap(QPixmap("images/Logo_Koalicja_Obywatelska_2023.svg.png"))
        self.label_3.setScaledContents(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(720, 290, 51, 21))
        self.label_5.setPixmap(QPixmap("images/Lewica_01.svg.png"))
        self.label_5.setScaledContents(True)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(890, 280, 61, 31))
        self.label_7.setPixmap(QPixmap("images/Konfederacja_03.svg.png"))
        self.label_7.setScaledContents(True)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(800, 290, 67, 17))
        self.label_9.setPixmap(QPixmap("images/Trzecia_Droga_logo.png"))
        self.label_9.setScaledContents(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(560, 280, 41, 41))
        self.label.setPixmap(QPixmap("images/Logo_PiS_Jasne.png"))
        self.label.setScaledContents(True)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QRect(40, 10, 271, 31))
        font = QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(130, 300, 89, 25))
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setGeometry(QRect(420, 50, 731, 221))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QRect(610, 0, 371, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.label_14.setGeometry(QRect(990, 280, 41, 31))
        self.label_14.setPixmap(
            QPixmap("images/Mniejszo\u015b\u0107_Niemiecka.svg.png")
        )
        self.label_14.setScaledContents(True)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.label_15.setGeometry(QRect(570, 360, 131, 17))
        self.label_PiSKonf = QLabel(self.centralwidget)
        self.label_PiSKonf.setObjectName("label_PiSKonf")
        self.label_PiSKonf.setGeometry(QRect(720, 360, 67, 17))
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(QRect(910, 360, 71, 17))
        self.label_Opposition = QLabel(self.centralwidget)
        self.label_Opposition.setObjectName("label_Opposition")
        self.label_Opposition.setGeometry(QRect(990, 360, 67, 17))
        self.label_PiS = QLabel(self.centralwidget)
        self.label_PiS.setObjectName("label_PiS")
        self.label_PiS.setGeometry(QRect(550, 320, 67, 17))
        self.label_PiS.setAlignment(Qt.AlignCenter)
        self.label_KO = QLabel(self.centralwidget)
        self.label_KO.setObjectName("label_KO")
        self.label_KO.setGeometry(QRect(630, 320, 67, 17))
        self.label_KO.setAlignment(Qt.AlignCenter)
        self.label_Lewica = QLabel(self.centralwidget)
        self.label_Lewica.setObjectName("label_Lewica")
        self.label_Lewica.setGeometry(QRect(710, 320, 67, 17))
        self.label_Lewica.setAlignment(Qt.AlignCenter)
        self.label_TD = QLabel(self.centralwidget)
        self.label_TD.setObjectName("label_TD")
        self.label_TD.setGeometry(QRect(800, 320, 67, 17))
        self.label_TD.setAlignment(Qt.AlignCenter)
        self.label_Konfederacja = QLabel(self.centralwidget)
        self.label_Konfederacja.setObjectName("label_Konfederacja")
        self.label_Konfederacja.setGeometry(QRect(890, 320, 67, 17))
        self.label_Konfederacja.setAlignment(Qt.AlignCenter)
        self.label_MN = QLabel(self.centralwidget)
        self.label_MN.setObjectName("label_MN")
        self.label_MN.setGeometry(QRect(980, 320, 67, 17))
        self.label_MN.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 220, 271, 27))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.lineEdit_Konfederacja = QLineEdit(self.layoutWidget)
        self.lineEdit_Konfederacja.setObjectName("lineEdit_Konfederacja")

        self.horizontalLayout_5.addWidget(self.lineEdit_Konfederacja)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(40, 260, 271, 21))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName("label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")

        self.horizontalLayout_6.addWidget(self.textBrowser)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName("widget1")
        self.widget1.setGeometry(QRect(41, 60, 271, 27))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_2.setFont(font2)
        self.label_2.setTextFormat(Qt.AutoText)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_PiS = QLineEdit(self.widget1)
        self.lineEdit_PiS.setObjectName("lineEdit_PiS")

        self.horizontalLayout.addWidget(self.lineEdit_PiS)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName("widget2")
        self.widget2.setGeometry(QRect(40, 140, 271, 27))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lineEdit_Lewica = QLineEdit(self.widget2)
        self.lineEdit_Lewica.setObjectName("lineEdit_Lewica")

        self.horizontalLayout_3.addWidget(self.lineEdit_Lewica)

        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName("widget3")
        self.widget3.setGeometry(QRect(40, 100, 271, 27))
        self.horizontalLayout_2 = QHBoxLayout(self.widget3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget3)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_KO = QLineEdit(self.widget3)
        self.lineEdit_KO.setObjectName("lineEdit_KO")

        self.horizontalLayout_2.addWidget(self.lineEdit_KO)

        self.widget4 = QWidget(self.centralwidget)
        self.widget4.setObjectName("widget4")
        self.widget4.setGeometry(QRect(41, 181, 271, 27))
        self.horizontalLayout_4 = QHBoxLayout(self.widget4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget4)
        self.label_10.setObjectName("label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.lineEdit_TD = QLineEdit(self.widget4)
        self.lineEdit_TD.setObjectName("lineEdit_TD")

        self.horizontalLayout_4.addWidget(self.lineEdit_TD)

        self.label_error = QLabel(self.centralwidget)
        self.label_error.setObjectName("label_error")
        self.label_error.setGeometry(QRect(40, 340, 271, 20))
        self.label_error.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(0, 390, 1181, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.label_19.setGeometry(QRect(26, 420, 291, 31))
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGeometry(QRect(330, 410, 821, 381))
        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_17 = QLabel(self.page)
        self.label_17.setObjectName("label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_17)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.tableWidget_results = QTableWidget(self.page_2)
        self.tableWidget_results.setObjectName("tableWidget_results")
        self.tableWidget_results.setGeometry(QRect(325, 60, 491, 227))
        self.widget5 = QWidget(self.page_2)
        self.widget5.setObjectName("widget5")
        self.widget5.setGeometry(QRect(20, 20, 291, 371))
        self.verticalLayout_2 = QVBoxLayout(self.widget5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.widget5)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.label_map = QLabel(self.tab)
        self.label_map.setObjectName("label_map")
        self.label_map.setGeometry(QRect(0, 10, 281, 251))
        self.label_map.setScaledContents(True)
        self.label_boundaries = QLabel(self.tab)
        self.label_boundaries.setObjectName("label_boundaries")
        self.label_boundaries.setGeometry(QRect(6, 270, 271, 61))
        font3 = QFont()
        font3.setPointSize(12)
        self.label_boundaries.setFont(font3)
        self.label_boundaries.setAlignment(Qt.AlignCenter)
        self.label_boundaries.setWordWrap(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName("label_18")
        self.label_18.setGeometry(QRect(20, 20, 91, 17))
        self.label_population = QLabel(self.tab_2)
        self.label_population.setObjectName("label_population")
        self.label_population.setGeometry(QRect(140, 20, 101, 17))
        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName("label_20")
        self.label_20.setGeometry(QRect(20, 70, 101, 17))
        self.label_area = QLabel(self.tab_2)
        self.label_area.setObjectName("label_area")
        self.label_area.setGeometry(QRect(140, 70, 101, 17))
        self.label_21 = QLabel(self.tab_2)
        self.label_21.setObjectName("label_21")
        self.label_21.setGeometry(QRect(20, 120, 141, 17))
        self.label_density = QLabel(self.tab_2)
        self.label_density.setObjectName("label_density")
        self.label_density.setGeometry(QRect(140, 120, 101, 17))
        self.label_24 = QLabel(self.tab_2)
        self.label_24.setObjectName("label_24")
        self.label_24.setGeometry(QRect(20, 180, 241, 17))
        self.label_popmandate = QLabel(self.tab_2)
        self.label_popmandate.setObjectName("label_popmandate")
        self.label_popmandate.setGeometry(QRect(100, 210, 67, 17))
        self.label_popmandate.setAlignment(Qt.AlignCenter)
        self.label_26 = QLabel(self.tab_2)
        self.label_26.setObjectName("label_26")
        self.label_26.setGeometry(QRect(20, 250, 251, 20))
        self.label_voters_per_seat = QLabel(self.tab_2)
        self.label_voters_per_seat.setObjectName("label_voters_per_seat")
        self.label_voters_per_seat.setGeometry(QRect(100, 280, 67, 17))
        self.label_voters_per_seat.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.label_22 = QLabel(self.page_2)
        self.label_22.setObjectName("label_22")
        self.label_22.setGeometry(QRect(450, 310, 131, 17))
        self.label_mandates = QLabel(self.page_2)
        self.label_mandates.setObjectName("label_mandates")
        self.label_mandates.setGeometry(QRect(620, 310, 67, 17))
        self.label_attendance = QLabel(self.page_2)
        self.label_attendance.setObjectName("label_attendance")
        self.label_attendance.setGeometry(QRect(620, 350, 67, 17))
        self.label_23 = QLabel(self.page_2)
        self.label_23.setObjectName("label_23")
        self.label_23.setGeometry(QRect(450, 350, 141, 17))
        self.label_district = QLabel(self.page_2)
        self.label_district.setObjectName("label_district")
        self.label_district.setGeometry(QRect(330, 10, 481, 31))
        self.label_district.setFont(font1)
        self.label_district.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.districts = QListWidget(self.centralwidget)
        self.districts.setObjectName("districts")
        self.districts.setGeometry(QRect(25, 460, 291, 341))
        self.radioButton_mainScenario = QRadioButton(self.centralwidget)
        self.radioButton_mainScenario.setObjectName("radioButton_mainScenario")
        self.radioButton_mainScenario.setGeometry(QRect(360, 310, 151, 23))
        self.radioButton_mainScenario.setFont(font2)
        self.radioButton_mainScenario.setChecked(True)
        self.radioButton_flis = QRadioButton(self.centralwidget)
        self.radioButton_flis.setObjectName("radioButton_flis")
        self.radioButton_flis.setGeometry(QRect(360, 330, 112, 23))
        self.radioButton_flis.setFont(font2)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(350, 300, 161, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName("line_3")
        self.line_3.setGeometry(QRect(340, 310, 20, 51))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName("line_4")
        self.line_4.setGeometry(QRect(350, 350, 161, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName("line_5")
        self.line_5.setGeometry(QRect(500, 310, 20, 51))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1176, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Kalkulator wyborczy", None)
        )
        self.label_3.setText("")
        self.label_5.setText("")
        self.label_7.setText("")
        self.label_9.setText("")
        self.label.setText("")
        self.label_12.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" text-decoration: underline;">Wpisz wyniki wybor\u00f3w</span></p></body></html>',
                None,
            )
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "Oblicz", None)
        )
        self.label_13.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" text-decoration: underline;">Podzia\u0142 mandat\u00f3w</span></p></body></html>',
                None,
            )
        )
        self.label_14.setText("")
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", "PiS + Konfederacja:", None)
        )
        self.label_PiSKonf.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "Opozycja:", None)
        )
        self.label_Opposition.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.label_PiS.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p>0</p></body></html>", None
            )
        )
        self.label_KO.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_Lewica.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_TD.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_Konfederacja.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.label_MN.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Konfederacja</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_Konfederacja.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.label_11.setText(QCoreApplication.translate("MainWindow", "Inne", None))
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600; color:#1a5fb4;">Prawo i Sprawiedliwo\u015b\u0107</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_PiS.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600; color:#ed333b;">Nowa Lewica                 </span></p></body></html>',
                None,
            )
        )
        self.lineEdit_Lewica.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600; color:#ff7800;">Koalicja Obywatelska    </span></p></body></html>',
                None,
            )
        )
        self.lineEdit_KO.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600; color:#33d17a;">Trzecia Droga</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_TD.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_error.setText("")
        self.label_19.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" text-decoration: underline;">Wybierz okr\u0119g wyborczy</span></p></body></html>',
                None,
            )
        )
        self.label_17.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#77767b;">Aby zobaczyć widok okręgu wpisz wynik wyborów w scenariuszu głównym i wybierz okrąg</span></p></body></html>',
                None,
            )
        )
        self.label_map.setText("")
        self.label_boundaries.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Mapa okr\u0119gu", None),
        )
        self.label_18.setText(
            QCoreApplication.translate("MainWindow", "Populacja:", None)
        )
        self.label_population.setText("")
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", "Powierzchnia:", None)
        )
        self.label_area.setText("")
        self.label_21.setText(
            QCoreApplication.translate("MainWindow", "G\u0119sto\u015b\u0107: ", None)
        )
        self.label_density.setText("")
        self.label_24.setText(
            QCoreApplication.translate(
                "MainWindow", "Liczba mieszka\u0144c\u00f3w na mandat:", None
            )
        )
        self.label_popmandate.setText("")
        self.label_26.setText(
            QCoreApplication.translate(
                "MainWindow", "Wzgl\u0119dna (do Warszawy) si\u0142a g\u0142osu:", None
            )
        )
        self.label_voters_per_seat.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Informacje o okr\u0119gu", None),
        )
        self.label_22.setText(
            QCoreApplication.translate("MainWindow", "Liczba mandat\u00f3w:", None)
        )
        self.label_mandates.setText("")
        self.label_attendance.setText("")
        self.label_23.setText(
            QCoreApplication.translate("MainWindow", "Frekwencja w 2019:", None)
        )
        self.label_district.setText("")
        self.radioButton_mainScenario.setText(
            QCoreApplication.translate(
                "MainWindow", "Scenariusz g\u0142\u00f3wny", None
            )
        )
        self.radioButton_flis.setText(
            QCoreApplication.translate("MainWindow", "Wz\u00f3r Flisa", None)
        )

    # retranslateUi
