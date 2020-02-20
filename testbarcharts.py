from barchart import BarChart
import matplotlib.pylab as plt
from multibarchart import MultiBarChart


def run_test():
    # a = BarChart([3, 5, 9, 2, 6, 15], {'a', 'b', 'c', 'd', 'e', 'f'})
    # a.basic_bar_chart('Usage', 'Programming language usage')
    # plt.show()
    # a = BarChart([3, 5, 9, 2, 6, 15], {'a', 'b', 'c', 'd', 'e', 'f'})
    # b = BarChart([20, 19, 35, 27, 16, 15], {'1', '2', '3', '4', '5', '6'})
    list_x = [[3, 5, 9, 2, 6, 15], [20, 19, 35, 27, 16, 15], [23, 5, 13, 4, 20, 40]]
    # c = BarChart([3, 5, 9, 2, 6, 15], {'q', 'w', 'e', 'r', 't', 'y'})
    c = MultiBarChart(list_x, {'a', 'b', 'c', 'd', 'e', 'f'}, ['var1', 'var2', 'var3'])
    c.multi_bar('test')
    # # c.basic_bar_chart()
    # plt.legend()
    # plt.show()
    # a.multi_bar('var1')
    # b.multi_bar('var2')
    plt.legend()
    plt.show()

run_test()
