from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()

        pg.plot([1, 2, 3, 4, 5])



