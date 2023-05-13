from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QVBoxLayout, QHBoxLayout
from instr import *
from second_win import *


class Expirement():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
        



class MainWin(QWidget):
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
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
        
    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()


        self.tw = TestWin()
        class TestWin(QWidget):
            def next_click(self):
                self.hide()
                self.exp = Expirement(self.line_age.text(),self.line_test1.text(),self.line_test2.text(),self.line_test3.text())
                self.tw = FinalWin(self.exp)

app = QApplication([]) #Создание приложения
zx=MainWin()
zx.initUI()

app.exec_() #Пока не нажат крестик - приложение работает(Всегда в конце)
