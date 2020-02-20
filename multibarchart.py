import numpy as np
import matplotlib.pylab as plt
list_colors = [(0.45, 0.58, 0.8), (0.88, 0.59, 0.3), (0.52, 0.73, 0.36), (0.83, 0.37, 0.38), (0.5, 0.52, 0.52), (0.56, 0.4, 0.65), (0.67, 0.41, 0.34), (0.8, 0.76, 0.06)]
barWidth = 0.25


class MultiBarChart:

    def __init__(self, list_x=None, objects=None, label_name=None, x_name=''):
        self.list_x = list_x
        self.label_name = label_name
        self.objects = objects
        self.x_name = x_name

    def get_color(self, value=0):
        colors = []
        for number in range(value):
            color = list_colors[number]
            colors.append(color)
        return colors

    def multi_bar(self, title=''):
        basic_position = np.arange(len(self.list_x[0]))
        list_position = [basic_position]
        for i in range(len(self.list_x)):
            position = [x + barWidth*(i+1) for x in basic_position]
            list_position.append(position)
        for i in range(len(self.list_x)):
            plt.bar(list_position[i], self.list_x[i], color=self.get_color(len(self.list_x)), width=barWidth, edgecolor='white', label=self.label_name[i])
        plt.xlabel(self.x_name, fontweight='bold')
        plt.title(title)
