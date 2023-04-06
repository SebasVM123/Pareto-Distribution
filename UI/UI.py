import sys
from PARETO.ParetoChart import *
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pareto.ui', self)

        self.move(200, 100)

        with open('stylesheet.qss') as f:
            self.setStyleSheet(f.read())

        self.lineEditAlpha.setValidator(QtGui.QDoubleValidator(0.0, 1000.0, 6))
        self.lineEditScale.setValidator(QtGui.QDoubleValidator(0.0, 1000.0, 6))

        self.pushButtonPlot.clicked.connect(self.plot)

    def plot(self):
        Xm = self.lineEditScale.text()
        alpha = self.lineEditAlpha.text()
        x = self.lineEditX.text()

        if(Xm == '' or alpha == '' or x == ''):
            popUp = QMessageBox()
            popUp.setWindowTitle('Error')
            popUp.setIcon(QMessageBox.Critical)
            popUp.setText('Empty Fields')
            popUp.show()
            popUp.exec_()
        elif(',' in Xm or ',' in alpha or ',' in x):
            popUp = QMessageBox()
            popUp.setWindowTitle('Warning')
            popUp.setIcon(QMessageBox.Warning)
            popUp.setText('Use points to represent floats.')
            popUp.show()
            popUp.exec_()
        else:
            Xm = float(Xm)
            alpha = float(alpha)
            x = float(x)

            if (Xm <= 0 or alpha <= 0):
                popUp = QMessageBox()
                popUp.setWindowTitle('Error')
                popUp.setIcon(QMessageBox.Critical)
                popUp.setText('Both parameters must be greater than 0')
                popUp.show()
                popUp.exec_()
            else:
                fig = ParetoDistribution(Xm, alpha, x)
                fig.close()
                fig.draw()

                if math.isinf(fig.mean):
                    self.labelMean.setStyleSheet('font-size: 20pt;')
                    self.labelMean.setText('∞')
                else:
                    self.labelMean.setStyleSheet('font-size: 14pt;')
                    self.labelMean.setText(str(fig.mean))

                self.labelMedian.setText(str(fig.median))

                if math.isinf(fig.variance):
                    self.labelVariance.setStyleSheet('font-size: 20pt;')
                    self.labelVariance.setText('∞')
                else:
                    self.labelVariance.setStyleSheet('font-size: 14pt;')
                    self.labelVariance.setText(str(fig.variance))

                if math.isinf(fig.skewness):
                    self.labelSkewness.setStyleSheet('font-size: 20pt;')
                    self.labelSkewness.setText('∞')
                else:
                    self.labelSkewness.setStyleSheet('font-size: 14pt;')
                    self.labelSkewness.setText(str(fig.skewness))

                if math.isinf(fig.kurtosis):
                    self.labelKurtosis.setStyleSheet('font-size: 20pt;')
                    self.labelKurtosis.setText('∞')
                else:
                    self.labelKurtosis.setStyleSheet('font-size: 14pt;')
                    self.labelKurtosis.setText(str(fig.kurtosis))

                self.labelFX.setText(str(fig.fx))