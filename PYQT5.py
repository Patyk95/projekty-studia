import sys
import numpy as np
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5 import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt



class ApplicationWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main= QWidget()
        self.setCentralWidget(self.main)

        layout= QHBoxLayout(self.main)



        self.figure =Figure(figsize=(6,6))
        self.ax =self.figure.subplots()

        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        side_layout=QVBoxLayout(self.main)
        layout.addLayout(side_layout)

        #rysowanie obiektu
        self.calculate_button = QPushButton('Rysuj')
        self.calculate_button.clicked.connect(self.calculate_slot)
        self.calculate_button.resize(620,400)
        side_layout.addWidget(self.calculate_button)

        #podawanie funkcji
        self.button1= QLineEdit(self)
        side_layout.addWidget(self.button1)


        #wybór min
        self.button2 = QDoubleSpinBox(self)
        side_layout.addWidget(self.button2)

        #wybór max
        self.button3 = QDoubleSpinBox(self)
        side_layout.addWidget(self.button3)

        #step
        self.button4 = QDoubleSpinBox(self)
        side_layout.addWidget(self.button4)

        side_layout.addStretch(1)

        #self.show()

    def calculate_slot(self):
        self.ax.clear()
        m = self.button3.valueChanged()
        s = self.button4.valueChanged()
        x = np.linspace(n,m,s)
        w = self.button1.textChanged()
        self.ax.plot(x, w)
        self.ax.grid(linestyle='--', alpha=0.5)
        self.figure.canvas.draw()






    def calculate_slot(self):
        self.ax.clear()
        x=np.linspace(-np.pi,np.pi,100) 
        y=np.sin(x)
        self.ax.plot(x,y)
        self.ax.grid(linestyle='--', alpha=0.5)
        self.figure.canvas.draw()


if __name__ == "__main__":

    qapp = QApplication.instance()

if not qapp:
    qapp = QApplication(sys.argv)
app= ApplicationWindow()
app.setWindowTitle("Aplikacja")
app.show()
app.activateWindow()
app.raise_()
qapp.exec()


