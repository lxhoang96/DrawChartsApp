import matplotlib.pylab as plt
import numpy as np
import pandas as pd


class BoxPlot:

    def __init__(self, values=None, objects=None, title='', position=''):
        self.values = values
        self.objects = objects
        self.title = title
        self.position = position
        self.basic_position = np.arange(len(self.objects))
        self.data = np.array(self.values)

    def box_plot(self, bar_name=''):
        plt.title(self.title)
        if self.position == 'vertical':
            bplot = plt.boxplot(self.data, 0, 'rs', vert=True, positions=self.basic_position, patch_artist=True)
            plt.xticks(self.basic_position, self.objects)
            plt.ylabel(bar_name)
            for patch in bplot['boxes']:
                patch.set(color='green')
            for median in bplot['medians']:
                median.set(color='black')
        elif self.position == 'horizontal':
            bplot = plt.boxplot(self.data, 0, 'rs', vert=False, positions=self.basic_position, patch_artist=True)
            plt.yticks(self.basic_position, self.objects)
            plt.xlabel(bar_name)
            for patch in bplot['boxes']:
                patch.set(color='green')
            for median in bplot['medians']:
                median.set(color='black')
