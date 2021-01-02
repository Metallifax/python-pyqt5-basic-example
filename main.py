from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def my_clicked():
  print('clicked')

def window():
  # Config
  app = QApplication(sys.argv)
  win = QMainWindow()
  win.setGeometry(800, 400, 300, 300)
  win.setWindowTitle('Tech With Tim')

  # Labels
  label = QtWidgets.QLabel(win)
  label.setText('My first label')
  label.move(50, 50)

  # Buttons
  b1 = QtWidgets.QPushButton(win)
  b1.setText('Click me!')
  b1.move(50, 75)
  b1.clicked.connect(my_clicked)

  # Start
  win.show()
  sys.exit(app.exec_())

window()