from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow, self).__init__()
    self.setGeometry(800, 400, 300, 300)
    self.setWindowTitle('Tech With Tim')
    self.initUI()

  def initUI(self):
    # Labels
    self.label = QtWidgets.QLabel(self)
    self.label.setText('My first label')
    self.label.move(50, 50)

      # Buttons
    self.b1 = QtWidgets.QPushButton(self)
    self.b1.setText('Click me!')
    self.b1.move(50, 75)
    self.b1.clicked.connect(self.clicked)

  def clicked(self):
    if self.label.text() == 'You pressed the button':
      self.label.setText("You pressed the button again!")
      self.update()
    else:
      self.label.setText("You pressed the button")
      self.update()

  def update(self):
    self.label.adjustSize()

def window():
  # Config
  app = QApplication(sys.argv)
  win = MyWindow()

  # Start
  win.show()
  sys.exit(app.exec_())

window()