import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import pareto


class ParetoDistribution:
    def __init__(self, Xm, alpha, x):
        self.Xm = Xm
        self.alpha = alpha
        self.mean = round(pareto.mean(self.alpha, loc=0, scale=self.Xm), 4)
        self.median = round(pareto.median(self.alpha, loc=0, scale=self.Xm), 4)
        self.variance = round(pareto.var(self.alpha, loc=0, scale=self.Xm), 4)
        self.skewness = round(self.skewnessCompute(), 4)
        self.kurtosis = round(self.kurtosisCompute(), 4)
        self.fx = self.image(x)

    def image(self, x):
        fx = pareto.cdf(x=x, b=self.alpha, loc=0, scale=self.Xm)
        return fx

    def draw(self):
        samples = np.linspace(start=self.Xm, stop=self.Xm+5, num=1000)
        pdf = np.array([pareto.pdf(x=samples, b=self.alpha, loc=0, scale=self.Xm)])
        cdf = np.array([pareto.cdf(x=samples, b=self.alpha, loc=0, scale=self.Xm)])
        linePDF = plt.plot(samples, pdf.T, color='#76323F', linewidth=3)
        lineCDF= plt.plot(samples, cdf.T, color='#C09F80', linewidth=3)

        plt.xlabel('Samples', fontsize=12)
        plt.grid(b=True, color='grey', alpha=0.5, linestyle='-.', linewidth=1)
        plt.legend(['Density function', 'Distribution function'], loc=5)
        plt.get_current_fig_manager().window.setGeometry(743, 131, 541, 473)
        plt.show()

    #Método que calcula la skewness
    def skewnessCompute(self):
        #Se crea una variable local para alpha
        a = self.alpha

        #Si alpha es mayor a 3 se calcula la skewness con la fórmula sino skewness es igual a infinito
        if a > 3:
            skewness = ((2 * (1 + a)) / (a - 3)) * (np.sqrt((a - 2) / (a)))
        else:
            skewness = np.inf

        return skewness

    #Método que calcula kurtosis
    def kurtosisCompute(self):
        #Se crea una variable local para alpha
        a = self.alpha

        #Si alpha es mayor a 4 se calcula la kurtosis con la fórmula sino kurtosis es igual a infinito
        if a > 4:
            kurtosis = (6 * (a**3 + a**2 - (6 * a) - 2)) / (a * (a - 3) * (a - 4))
        else:
            kurtosis = np.inf

        return kurtosis

    #Cierra la ventana del gráfico
    def close(self):
        plt.close()