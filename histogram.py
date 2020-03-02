import matplotlib.pylab as plt
import pandas as pd
import numpy as np


class Histogram:

    def __init__(self, values=None):
        self.values = values

    def basic_histogram(self, xname='', yname='', title=''):
        plt.hist(self.values, bins='auto')
        plt.xticks(xname)
        plt.yticks(yname)
        plt.title(title)
