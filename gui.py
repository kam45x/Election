from PySide2.QtWidgets import QMainWindow, QListWidgetItem
from PySide2.QtWidgets import QGraphicsScene, QGraphicsProxyWidget
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtGui import QColor, QFont

from ui_election_calculator import Ui_MainWindow
from district_database import DistrictDatabase
from constants import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class ElectionCalculatorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._is_user_data_proper = False
        self._is_main_scenario = True

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__init_database()
        self.__init_mandates_chart()
        self.__init_list_of_distrcits()

        # Set map widget as default
        self.ui.tabWidget.setCurrentWidget(self.ui.tab)
        # Monitor button click
        self.ui.pushButton.clicked.connect(self._calculate_mandates)

    def __init_database(self):
        self.database = DistrictDatabase(
            districts_path="okregi_sejm.csv",
            parlamentary2019_election_path="wyniki_gl_na_listy_po_okregach_sejm.csv",
            presidential2020_election_path="districts_results_2020_AUTO.csv",
            list_leaders_path="jedynki.csv",
            population_path="ludnosc_2022.csv",
            area_path="powierzchnia.csv",
        )

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
        self._reset_party_labels()
        self._is_user_data_proper = True

        # Check if user data is not empty
        if self._is_all_user_data_zeroes():
            self.ui.label_error.setText(
                "<b><font color='red'>BŁĄD: Wprowadź jakieś wyniki!<b></font>"
            )
            self._error_action()
            return

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
            self._error_action()
            return

        # Check if all values are non-negative
        for percent in poll_results_percent.values():
            if percent < 0:
                self.ui.label_error.setText(
                    "<b><font color='red'>BŁĄD: Wprowadź nieujemne wartości!<b></font>"
                )
                self._error_action()
                return

        # Sum can be larger than 100% (because of MN) - it wil be rescaled
        poll_results_percent["Inne"] = (
            100 + poll_results_percent["MN"] - sum(poll_results_percent.values())
        )
        self.ui.textBrowser.setText(f"{round(poll_results_percent['Inne'], 1)}")

        # Check if sum is not larger than 100% (plus MN)
        if poll_results_percent["Inne"] < 0:
            self.ui.label_error.setText(
                "<b><font color='red'>BŁĄD: Suma przekracza 100%!<b></font>"
            )
            self._error_action()
            return

        # Calculate mandates
        if self.ui.radioButton_mainScenario.isChecked():
            self._is_main_scenario = True
            self.database.simulate_poll_results(poll_results_percent, 0.01)
            mandates = self.database.get_number_of_mandates()
        elif self.ui.radioButton_flis.isChecked():
            self._is_main_scenario = False
            mandates = self.database.get_number_of_mandates_flis(poll_results_percent)

        # Update
        self._update_mandates_chart(mandates)
        self._update_mandate_labels(mandates)
        self._update_districts_info()

    def _update_mandates_chart(self, party_mandates):
        parties = []
        chart_mandates = []

        for party, n_mandates in party_mandates.items():
            if party != "Inne":
                parties.append(party)
                chart_mandates.append(n_mandates)

        self.ax.bar(parties, chart_mandates)
        self.canvas = FigureCanvas(self.figure)
        self.proxy = QGraphicsProxyWidget()
        self.proxy.setWidget(self.canvas)

        self.proxy.setPos(self.x, self.y)
        self.canvas.setGeometry(
            0, 0, self.view_rect.width() - 5, self.view_rect.height() - 5
        )
        self.scene.addItem(self.proxy)

    def _update_mandate_labels(self, mandates):
        self.ui.label_PiS.setText(f"<font color='blue'>{mandates['PiS']}</font>")
        self.ui.label_KO.setText(f"<font color='orange'>{mandates['KO']}</font>")
        self.ui.label_Lewica.setText(f"<font color='red'>{mandates['Lewica']}</font>")
        self.ui.label_TD.setText(f"<font color='green'>{mandates['TD']}</font>")
        self.ui.label_Konfederacja.setText(f"{mandates['Konfederacja']}")
        self.ui.label_MN.setText(f"<font color='grey'>{mandates['MN']}</font>")

        mandates_PiSKonfederacja = 0
        mandates_Opposition = 0

        for party in mandates:
            if party in PIS_KONFEDERACJA:
                mandates_PiSKonfederacja += mandates[party]
            elif party in OPPOSITION:
                mandates_Opposition += mandates[party]

        # Check majority of mandates
        if mandates_PiSKonfederacja > 230:
            self.ui.label_PiSKonf.setText(f"<b>{mandates_PiSKonfederacja}<b>")
        else:
            self.ui.label_PiSKonf.setText(f"{mandates_PiSKonfederacja}")

        if mandates_Opposition > 230:
            self.ui.label_Opposition.setText(f"<b>{mandates_Opposition}<b>")
        else:
            self.ui.label_Opposition.setText(f"{mandates_Opposition}")

    def _update_districts_info(self):
        if self._is_user_data_proper and self._is_main_scenario:
            if self.ui.districts.currentItem() is not None:
                self._select_district(self.ui.districts.currentItem())
        else:
            self._reset_stacked_widget()

    def _select_district(self, item):
        if self._is_user_data_proper and self._is_main_scenario:
            # Change page
            self.ui.stackedWidget.setCurrentIndex(1)
            # Set district name
            self.ui.label_district.setText(f"{item.district}")
            # Set district map
            self.ui.label_map.setPixmap(
                f"images/Sejm_RP_{item.district.get_id()}.svg.png"
            )

            self._update_district_results_table(item)
            self._update_district_labels(item)

    def _update_district_results_table(self, item):
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
        self.ui.tableWidget_results.setColumnWidth(0, 116)
        self.ui.tableWidget_results.setColumnWidth(1, 200)
        self.ui.tableWidget_results.setColumnWidth(2, 80)
        self.ui.tableWidget_results.setColumnWidth(3, 80)
        # Row height
        for i in range(n_parties - 1):
            self.ui.tableWidget_results.setRowHeight(i, 34)

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
                )  # Set background party color
                self.ui.tableWidget_results.setItem(row, 0, party_item)

                leader_item = QTableWidgetItem(
                    f"{item.district.get_list_leader(party)}"
                )
                leader_item.setTextAlignment(4)  # Center text
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

    def _update_district_labels(self, item):
        # Display big cities in district
        boundaries_text = ""
        boundaries_powiats = item.district.get_boundaries_description().split(", ")
        if len(boundaries_powiats) > 1:
            for powiat in boundaries_powiats:
                if powiat[0].isupper():
                    boundaries_text += f"{powiat}, "
            boundaries_text = boundaries_text.removesuffix(", ")
        else:
            boundaries_text = boundaries_powiats[0]
        self.ui.label_boundaries.setText(boundaries_text)

        self.ui.label_mandates.setText(f"{item.district.get_n_seats()}")

        self.ui.label_attendance.setText(
            f"{round(item.district.get_attendance_percent(), 2)}%"
        )

        relative_vote_strength = (
            self.database.get_district("19").get_votes_per_seat()
            / item.district.get_votes_per_seat()
        )
        self.ui.label_voters_per_seat.setText(f"{round(relative_vote_strength, 2)}")

        self.ui.label_population.setText(
            f"{int(item.district.get_population() / 1000)} tys."
        )
        self.ui.label_area.setText(f"{item.district.get_area()} km2")
        self.ui.label_density.setText(
            f"{int(item.district.get_population() / item.district.get_area())} os./km2"
        )

        self.ui.label_popmandate.setText(
            f"{round((item.district.get_population() / item.district.get_n_seats()) / 1000, 1)} tys."
        )

    def _is_all_user_data_zeroes(self):
        return (
            self.ui.lineEdit_PiS.text() == "0"
            and self.ui.lineEdit_KO.text() == "0"
            and self.ui.lineEdit_Lewica.text() == "0"
            and self.ui.lineEdit_TD.text() == "0"
            and self.ui.lineEdit_Konfederacja.text() == "0"
        )

    def _reset_stacked_widget(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def _reset_party_labels(self):
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

    def _error_action(self):
        self._is_user_data_proper = False
        self._reset_stacked_widget()
