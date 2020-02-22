import matplotlib.pylab as plt
import numpy as np
import statistics
list_colors = [(0.45, 0.58, 0.8), (0.88, 0.59, 0.3), (0.52, 0.73, 0.36), (0.83, 0.37, 0.38), (0.5, 0.52, 0.52), (0.56, 0.4, 0.65), (0.67, 0.41, 0.34), (0.8, 0.76, 0.06)]
barWidth = 0.5


class BarChart:
    def __init__(self, x=None, objects=None, title='', position=''):
        self.x = x
        self.objects = objects
        self.title = title
        self.position = position
        self.basic_position = np.arange(len(self.objects))
        self.data = []
        for i in range(len(self.x)):
            data = np.array(self.x[i])
            self.data.append(data)

    def get_color(self, value=0):
        colors = []
        for number in range(value):
            color = list_colors[number]
            colors.append(color)
        return colors

    def basic_bar_chart(self, unit=''):
        plt.title(self.title)
        if self.position == 'vertical':
            plt.bar(self.basic_position, self.data, align='center', color=self.get_color(len(self.objects)))
            plt.xticks(self.basic_position, self.objects)
            plt.ylabel(unit)
        elif self.position == 'horizontal':
            plt.barh(self.basic_position, self.data, align='center', color=self.get_color(len(self.objects)))
            plt.yticks(self.basic_position, self.objects)
            plt.xlabel(unit)
        else:
            print('Not supported')

    def multi_bar(self, label_name=None, x_name=''):
        list_position = [self.basic_position]
        plt.title(self.title)
        bar = []
        for i in range(len(self.data)):
            position = [x + barWidth*(i+1) for x in self.basic_position]
            list_position.append(position)
        if self.position == 'vertical':
            for i in range(len(self.data)):
                p = plt.bar(list_position[i], self.data[i], color=list_colors[i], width=barWidth, edgecolor='white', label=label_name[i])
                bar.append(p)
            plt.xticks(self.basic_position + barWidth*int(len(self.x)/2), self.objects)
            plt.xlabel(x_name, fontweight='bold')
        elif self.position == 'horizontal':
            for i in range(len(self.data)):
                p = plt.barh(list_position[i], self.data[i], color=list_colors[i], width=barWidth, edgecolor='white', label=label_name[i])
                bar.append(p)
            plt.yticks(self.basic_position + barWidth*int(len(self.data)/2), self.objects)
            plt.ylabel(x_name, fontweight='bold')
        plt.legend(bar, label_name)

    def stacked_bar(self, bar_name=''):
        plt.title(self.title)
        bar = []
        bottom = 0
        if self.position == 'vertical':
            p = plt.bar(x=self.basic_position, height=self.data[0], width=barWidth, color=list_colors[0], align='center', yerr=1)
            bar.append(p)
            plt.xticks(ticks=self.basic_position, lable=self.objects)
            for i in range(1, len(self.data)):
                bottom += self.data[i-1]
                p1 = plt.bar(x=self.basic_position, height=self.data[i], width=barWidth, bottom=bottom, color=list_colors[i], align='center', yerr=1)
                bar.append(p1)
        elif self.position == 'horizontal':
            p0 = plt.barh(y=self.basic_position, width=self.data[0], height=barWidth, color=list_colors[0], align='center', xerr=1)
            bar.append(p0)
            plt.yticks(ticks=self.basic_position, label=self.objects)
            for i in range(1, len(self.data)):
                bottom += self.data[i-1]
                p2 = plt.barh(y=self.basic_position, width=self.data[i], height=barWidth, left=bottom, color=list_colors[i], align='center', xerr=1)
                bar.append(p2)
        plt.legend(bar, bar_name)
