from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QFont
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




    def timer_test(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def connects(self):
        self.button.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
        self.button3.clicked.connect(self.timer_final)
    def timer_sits(self):
        time = QTime(0,0,30)
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer2Event(self):
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])

    def timer_final(self):
        time = QTime(0,1,0)
        self.timer.timeout.connect(self.timer3Event)
    
    def timer3Event(self):
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")

    def next_click(self):
        self.hide()


    

class FinalWin(QWidget):
    def __init__(self, exp):
        pass


app = QApplication([])
zx2=MainWin()
zx2.initUI()

app.exec_() #Пока не нажат крестик - приложение работает(Всегда в конце)
