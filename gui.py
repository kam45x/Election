from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide2.QtWidgets import QGraphicsScene, QGraphicsProxyWidget
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtGui import QColor, QFont
import sys

from ui_election_calculator import Ui_MainWindow
from district_database import DistrictDatabase
from constants import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class ElectionCalculatorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database = DistrictDatabase(
            "okregi_sejm.csv",
            "wyniki_gl_na_listy_po_okregach_sejm.csv",
            "districts_results_2020_AUTO.csv",
            "jedynki.csv",
        )
        self.__init_mandates_chart()
        self.__init_list_of_distrcits()

        # Monitor button click
        self.ui.pushButton.clicked.connect(self._calculate_mandates)

    def __init_mandates_chart(self):
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.proxy = QGraphicsProxyWidget()
        self.proxy.setWidget(self.canvas)

        self.view_rect = self.ui.graphicsView.rect()
        self.chart_rect = self.canvas.rect()
        self.x = (self.view_rect.width() - self.chart_rect.width()) / 2
        self.y = (self.view_rect.height() - self.chart_rect.height()) / 2

    def __init_list_of_distrcits(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        for district in self.database.get_districts():
            item = QListWidgetItem(f"{district}")
            item.district = district
            self.ui.districts.addItem(item)
        self.ui.districts.itemClicked.connect(self._select_district)

    def _calculate_mandates(self):
        self._reset()

        try:
            poll_results_percent = {
                "PiS": float(self.ui.lineEdit_PiS.text()),
                "KO": float(self.ui.lineEdit_KO.text()),
                "Lewica": float(self.ui.lineEdit_Lewica.text()),
                "TD": float(self.ui.lineEdit_TD.text()),
                "Konfederacja": float(self.ui.lineEdit_Konfederacja.text()),
                "MN": 0.17,
            }
        except ValueError:
            self.ui.label_error.setText(
                "<b><font color='red'>BŁĄD: Wprowadź poprawne wartości!<b></font>"
            )
            return

        # Sum can be larger than 100% (because of MN) - it wil be rescaled
        poll_results_percent["Inne"] = (
            100 + poll_results_percent["MN"] - sum(poll_results_percent.values())
        )
        self.ui.textBrowser.setText(f"{round(poll_results_percent['Inne'], 1)}")

        if poll_results_percent["Inne"] < 0:
            self.ui.label_error.setText(
                "<b><font color='red'>BŁĄD: Suma przekracza 100%!<b></font>"
            )
            return

        self.database.simulate_poll_results(poll_results_percent, 0.01)

        self._update_mandates_chart()
        self._update_mandate_labels()

    def _update_mandates_chart(self):
        parties = []
        mandates = []

        for party, mandates_ in self.database.get_number_of_mandates().items():
            if party != "Inne":
                parties.append(party)
                mandates.append(mandates_)

        self.ax.bar(parties, mandates)
        self.canvas = FigureCanvas(self.figure)
        self.proxy = QGraphicsProxyWidget()
        self.proxy.setWidget(self.canvas)

        self.proxy.setPos(self.x, self.y)
        self.canvas.setGeometry(
            0, 0, self.view_rect.width() - 5, self.view_rect.height() - 5
        )
        self.scene.addItem(self.proxy)

    def _update_mandate_labels(self):
        self.ui.label_PiS.setText(
            f"<font color='blue'>{self.database.get_number_of_mandates()['PiS']}</font>"
        )
        self.ui.label_KO.setText(
            f"<font color='orange'>{self.database.get_number_of_mandates()['KO']}</font>"
        )
        self.ui.label_Lewica.setText(
            f"<font color='red'>{self.database.get_number_of_mandates()['Lewica']}</font>"
        )
        self.ui.label_TD.setText(
            f"<font color='green'>{self.database.get_number_of_mandates()['TD']}</font>"
        )
        self.ui.label_Konfederacja.setText(
            f"{self.database.get_number_of_mandates()['Konfederacja']}"
        )
        self.ui.label_MN.setText(
            f"<font color='grey'>{self.database.get_number_of_mandates()['MN']}</font>"
        )

        mandates_PiSKonfederacja = self.database.get_mandates_of_parties(
            PIS_KONFEDERACJA
        )
        mandates_Opposition = self.database.get_mandates_of_parties(OPPOSITION)

        # Check majority of mandates
        if mandates_PiSKonfederacja > 230:
            self.ui.label_PiSKonf.setText(f"<b>{mandates_PiSKonfederacja}<b>")
        else:
            self.ui.label_PiSKonf.setText(f"{mandates_PiSKonfederacja}")

        if mandates_Opposition > 230:
            self.ui.label_Opposition.setText(f"<b>{mandates_Opposition}<b>")
        else:
            self.ui.label_Opposition.setText(f"{mandates_Opposition}")

    def _select_district(self, item):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.label_district.setText(f"{item.district.get_name()}")

        n_parties = len(self.database.get_number_of_mandates())
        # Ignore "Inne" party
        self.ui.tableWidget_results.setRowCount(n_parties - 1)
        self.ui.tableWidget_results.setColumnCount(4)
        self.ui.tableWidget_results.setHorizontalHeaderLabels(
            ["Partia", "Nr 1 na liście", "Poparcie", "Mandaty"]
        )

        parties_mandates = item.district.get_number_of_mandates()
        # Sort parties by results
        parties_results_percent = dict(
            sorted(
                item.district.get_results_percent().items(),
                key=lambda item_: item_[1],
                reverse=True,
            )
        )

        # Column width
        self.ui.tableWidget_results.setColumnWidth(0, 120)
        self.ui.tableWidget_results.setColumnWidth(1, 200)
        self.ui.tableWidget_results.setColumnWidth(2, 80)
        self.ui.tableWidget_results.setColumnWidth(3, 80)

        row = 0
        for party, percent in parties_results_percent.items():
            if party != "Inne":
                party_item = QTableWidgetItem(f"{party}")
                # Bold font for party name
                font = QFont()
                font.setBold(True)
                party_item.setFont(font)
                party_item.setBackground(
                    QColor(
                        PARTY_COLORS[party][0],
                        PARTY_COLORS[party][1],
                        PARTY_COLORS[party][2],
                    )
                ) # Set background party color
                self.ui.tableWidget_results.setItem(row, 0, party_item)

                leader_item = QTableWidgetItem(
                    f"{item.district.get_list_leader(party)}"
                )
                leader_item.setTextAlignment(4) # Center text
                self.ui.tableWidget_results.setItem(row, 1, leader_item)

                results_item = QTableWidgetItem(f"{round(percent, 1)}%")
                results_item.setTextAlignment(4)
                self.ui.tableWidget_results.setItem(
                    row, 2, QTableWidgetItem(results_item)
                )

                mandates_item = QTableWidgetItem(f"{parties_mandates[party]}")
                mandates_item.setTextAlignment(4)
                self.ui.tableWidget_results.setItem(
                    row, 3, QTableWidgetItem(mandates_item)
                )

                row += 1

    def _reset(self):
        # Reset labels
        self.ui.label_error.setText("")
        self.ui.label_PiS.setText("0")
        self.ui.label_KO.setText("0")
        self.ui.label_Lewica.setText("0")
        self.ui.label_TD.setText("0")
        self.ui.label_Konfederacja.setText("0")
        self.ui.label_MN.setText("0")
        self.ui.label_PiSKonf.setText("0")
        self.ui.label_Opposition.setText("0")

        # Reset chart
        self.scene.clear()
        self.ax.clear()

        # Reset database
        self.database.reset_all_districts_state()


def guiMain(args):
    app = QApplication(args)
    window = ElectionCalculatorWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
