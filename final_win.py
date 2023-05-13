from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super()__init__()
        self.set_appear()
        self.initUI()

        self.show()

        def set_appear():
            self.setWindowTitle(txt_title)
            self.resize(win_width, win_height)
            self.move(win_x, win_y)


        def initUI():
            self.index = QLabel(txt_index)
            self.workheart = QLabel(txt_workheart)
            self.line = QVBoxLayout()
            self.line.addWidget(self.index, alignment=Qt.AlignCenter)
            self.line.addWidget(self.workheart, alignment=Qt.AlignCenter)
            self.setLayout(self.line)
            gnment=Qt.AlignCenter)
            self.setLayout(self.line)
            
