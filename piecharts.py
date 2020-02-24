import matplotlib.pylab as plt
import numpy as np


class PieCharts:

    def __init__(self, labels=None, sizes=None, explode=None):
        self.labels = labels
        self.sizes = sizes
        self.explode = explode

    def basic_pie_chart(self, title='', units=''):
        fig, ax = plt.subplots()

        wedges, texts, autotexts = ax.pie(self.sizes, explode=self.explode, labels=self.labels, autopct='%1.1f%%', startangle=90, textprops=dict(color='w'))
        ax.legend(wedges,  self.labels, title='Unit: {}'.format(units), loc='upper right')
        plt.setp(autotexts, size=8, weight='bold')
        ax.set_title(title, size=12)
        ax.axis('equal')
