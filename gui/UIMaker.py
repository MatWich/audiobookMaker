import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class UIMaker(QWidget):
    def __init__(self, parent=None):
        super(UIMaker, self).__init__(parent)
        self.file_path = None
        self.layout = QGridLayout()
        self.initUI()

    def initUI(self):
        """ CREATES ALL UI ELEMENTS"""
        file_hbox = QHBoxLayout()
        self.selectFileBtn = QPushButton('Select File')
        self.selectFileBtn.clicked.connect(self.get_file_name)
        self.file_path_lbl = QLabel("File not selected")

        file_hbox.addWidget(self.selectFileBtn)
        file_hbox.addWidget(self.file_path_lbl)

        """ SLIDERS"""
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        self.volume_lbl = QLabel("Volume")
        self.volume_slider = QSlider(Qt.Horizontal) # 0.01 - 1
        self.volume_slider.setMinimum(1)
        self.volume_slider.setMaximum(100)
        hbox1.addWidget(self.volume_lbl)
        hbox1.addWidget(self.volume_slider)

        hbox2 = QHBoxLayout()
        self.rate_lbl = QLabel("Rate")
        self.rate_slider = QSlider(Qt.Horizontal)
        self.rate_slider.setMinimum(100)
        self.rate_slider.setMaximum(300)
        hbox2.addWidget(self.rate_lbl)
        hbox2.addWidget(self.rate_slider)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.layout.addLayout(file_hbox, 0, 0)
        self.layout.addLayout(vbox, 1, 1)
        self.setLayout(self.layout)

    def get_file_name(self):
        """ Opens a file dialog and returns a path to a file"""
        file_flter = "Pdf file (*.pdf);; Any file (*.*)"
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a pdf file',
            directory=os.getcwd(),
            filter=file_flter,
            initialFilter="pdf file (*.pdf)"
        )
        self.file_path = response[0]
        print(f"file path: {self.file_path}")
        self.file_path_lbl.setText(response[0])
        print(response)
