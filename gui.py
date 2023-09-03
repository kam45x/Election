from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QGraphicsScene, QGraphicsProxyWidget
import sys

from ui_election_calculator import Ui_MainWindow
from district_database import DistrictDatabase
from constants import PIS_KONFEDERACJA, OPPOSITION

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
        )
        self.__init_mandates_chart()

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
            self.ui.label_error.setText("<b><font color='red'>BŁĄD: Wprowadź poprawne wartości!<b></font>")
            return

        # Sum can be larger than 100% (because of MN) - it wil be rescaled
        poll_results_percent["Inne"] = (
            100 + poll_results_percent["MN"] - sum(poll_results_percent.values())
        )
        self.ui.textBrowser.setText(f"{round(poll_results_percent['Inne'], 1)}")

        if poll_results_percent["Inne"] < 0:
            self.ui.label_error.setText("<b><font color='red'>BŁĄD: Suma przekracza 100%!<b></font>")
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
        self.ui.label_PiS.setText(f"<font color='blue'>{self.database.get_number_of_mandates()['PiS']}</font>")
        self.ui.label_KO.setText(f"<font color='orange'>{self.database.get_number_of_mandates()['KO']}</font>")
        self.ui.label_Lewica.setText(
            f"<font color='red'>{self.database.get_number_of_mandates()['Lewica']}</font>"
        )
        self.ui.label_TD.setText(f"<font color='green'>{self.database.get_number_of_mandates()['TD']}</font>")
        self.ui.label_Konfederacja.setText(
            f"{self.database.get_number_of_mandates()['Konfederacja']}"
        )
        self.ui.label_MN.setText(f"<font color='grey'>{self.database.get_number_of_mandates()['MN']}</font>")

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

    def _reset(self):
        # Reset labels
        self.ui.label_error.setText("0")
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
