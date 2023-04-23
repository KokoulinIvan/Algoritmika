# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox

from random import randint


title = 'С'
app = QApplication([])
main_win = QWidget()
main_win.resize(400, 200)
but = QPushButton('1')
but1 = QPushButton('2')
text1 = QLabel('')

h_line = QHBoxLayout()
h_line.addWidget(but, alignment = Qt.AlignCenter)
h_line.addWidget(but1, alignment = Qt.AlignCenter)
main_win.setLayout(h_line)



def win():
    win1 = QMessageBox()
    win1.setText('Победа!')
    win1.exec_()

def lose():
    lose1 = QMessageBox()
    lose1.setText('Проигрыш :(')
    lose1.exec_()

but.clicked.connect(win)
but1.clicked.connect(lose)

main_win.show()
app.exec_()