from PySide2.QtWidgets import QApplication
import sys

from gui import ElectionCalculatorWindow


def guiMain(args):
    app = QApplication(args)
    window = ElectionCalculatorWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
