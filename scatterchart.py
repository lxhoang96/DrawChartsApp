import seaborn as sns
import matplotlib.pylab as plt
import numpy as np
sns.set(color_codes=True)


class ScatterPlot:

    def __init__(self, values=None, objects=None, xlabel='', ylabel=''):
        self.x = values
        self.y = objects
        self.xlabel = xlabel
        self.ylabel = ylabel

    def basic_scatter_plot(self, reg=True, data=None):
        tips = sns.load_dataset('tips')
        sns.regplot(x=self.x, y=self.y, fit_reg=reg, data=data)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
