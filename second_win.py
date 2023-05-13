from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.fio = QLabel(txt_name)
        self.age = QLabel(txt_age)
        self.test1 = QLabel(txt_test1)
        self.test2 = QLabel(txt_test2)
        self.test3 = QLabel(txt_test3)
        self.timer = QLabel("Таймер")
        self.button1 = QPushButton(txt_starttest1)
        self.button2 = QPushButton(txt_starttest2)
        self.button3 = QPushButton(txt_starttest3)
        self.button_final = QPushButton(txt_sendresults)
        self.hint1 = QLineEdit(txt_hintname)
        self.hint2 = QLineEdit(txt_hintage)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)

        self.l_line.addWidget(self.fio, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.hint1, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.age, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.hint2, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.test1, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.button1, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.hinttest1, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.test2, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.button2, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.test3, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.button3, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.hinttest2, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.hinttest3, alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.timer, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.age, alignment=Qt.AlignCenter)
        
        self.h_line.addWidget(self.l_line,alignment=Qt.AlignCenter)
        self.h_line.addWidget(self.r_line,alignment=Qt.AlignCenter)
        self.setLayout(self.h_line)



    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()




class FinalWin(QWidget):
    def __init__(self, exp):
        pass


app = QApplication([])
zx2=MainWin()
zx2.initUI()

app.exec_() #Пока не нажат крестик - приложение работает(Всегда в конце)
