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
