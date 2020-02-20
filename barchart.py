import matplotlib.pylab as plt
import numpy as np

list_colors = [(0.45, 0.58, 0.8), (0.88, 0.59, 0.3), (0.52, 0.73, 0.36), (0.83, 0.37, 0.38), (0.5, 0.52, 0.52), (0.56, 0.4, 0.65), (0.67, 0.41, 0.34), (0.8, 0.76, 0.06)]


class BarChart:
    def __init__(self, x=None, objects=None):
        self.x = x
        self.objects = objects


    def get_color(self, value=0):
        colors = []
        for number in range(value):
            color = list_colors[number]
            colors.append(color)
        return colors

    def basic_bar_chart(self, unit='', title=''):
        y_value = np.arange(len(self.objects))
        plt.bar(y_value, self.x, align='center', alpha=0.5, color=self.get_color(len(self.objects)))
        plt.xticks(y_value, self.objects)
        plt.ylabel(unit)
        plt.title(title)
        plt.autoscale(tight=True)

