import matplotlib.pylab as plt
import numpy as np
# import pandas as pd


class BubbleChart:

    def __init__(self, values=None):
        self.values = values
        # self.objects = objects

    def basic_bubble(self, marked_line=False, line='', point=None):
        plt.scatter(self.values[0], self.values[1])
        if marked_line:
            if line == 'circle':
                theta = np.arange(0, np.pi / 2, 0.01)
                plt.plot(point[0][0] * np.cos(theta), point[1][1] * np.sin(theta), color='red')
            elif line == 'line':
                plt.plot(point[0], point[1], color='red')


