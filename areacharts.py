import matplotlib.pylab as plt


class AreaCharts:

    def __init__(self, objects=None, values=None, title='', x_name='', y_name=''):
        self.objects = objects
        self.values = values
        self.title = title
        self.x_name = x_name
        self.y_name = y_name

    def basic_chart(self, labels=None, location=''):
        fig, ax = plt.subplots()
        ax.stackplot(self.objects, self.values, labels=labels)
        ax.legend(loc=location)
        plt.title(self.title)
        plt.xlabel(self.x_name)
        plt.ylabel(self.y_name)
