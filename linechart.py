import matplotlib.pylab as plt


class LineChart:

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def basic_line_chart(self, name_x='', name_y=''):
        plt.plot(self.x, self.y, marker='o')
        plt.ylabel(name_y)
        plt.xlabel(name_x)





