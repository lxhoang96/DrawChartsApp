import matplotlib.pylab as plt


class AreaCharts:

    def __init__(self, objects=None, values=None):
        self.objects = objects
        self.values = values

    def basic_chart(self, labels=None, location=''):
        fig, ax = plt.subplots()
        ax.stackplot(self.objects, self.values, labels=labels)
        ax.legend(loc=location)
