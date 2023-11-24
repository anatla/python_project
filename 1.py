from PyQt5 import QtWidgets, uic
import sys
import pyqtgraph as pg
import matplotlib.pyplot as plt
import numpy as np

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('1.ui', self)

        self.pushButton.clicked.connect(self.calculate)
        self.show()

    def calculate(self):
        try:
            self.lineEdit_4.setText(str(float(self.lineEdit.text())+float(self.lineEdit_2.text())))
        except:
            self.lineEdit_4.setText("Error")

    # def graph(self):


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.setFixedWidth(220)
window.setFixedHeight(160)
app.exec_()
