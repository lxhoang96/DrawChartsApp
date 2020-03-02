import matplotlib.pylab as plt
import numpy as np
from boxplot import BoxPlot


def test():
    # Boxplot
    list_x1 = [[-0.46, -1.25, -2.62, 0.22], [0.24, 1.88, -0.49, -0.73, -0.49], [-0.44, 0.93, 0.19, -4.36, -0.88]]
    d = BoxPlot(list_x1, ['G1', 'G2', 'G3'], 'Test', 'vertical')
    d.box_plot('unit')
    plt.show()


test()
