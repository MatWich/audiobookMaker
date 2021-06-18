import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class UIMaker(QWidget):
    def __init__(self, parent=None):
        super(UIMaker, self).__init__(parent)
        self.layout = QGridLayout()
        self.initUI()

    def initUI(self):
        """ CREATES ALL UI ELEMENTS"""
        self.selectFileBtn = QPushButton('Select File')
        self.selectFileBtn.clicked.connect(self.get_file_name)

        self.layout.addWidget(self.selectFileBtn)
        self.setLayout(self.layout)

    def get_file_name(self):
        file_flter = "Pdf file (*.pdf);; Any file (*.*)"
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a pdf file',
            directory=os.getcwd(),
            filter=file_flter,
            initialFilter="pdf file (*.pdf)"
        )
        print(response)
