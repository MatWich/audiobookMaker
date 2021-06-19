from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from UIMaker import UIMaker


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setWindowTitle("Audiobook Maker")
        self.setMinimumWidth(600)
        self.setMinimumHeight(500)
        self.context_menu()

    def context_menu(self):
        """Create main menu"""
        self.UIMaker = UIMaker()
        self.setCentralWidget(self.UIMaker)
        self.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())