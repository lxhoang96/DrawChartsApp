from barchart import BarChart
import matplotlib.pylab as plt


def run_test():
    """
    Test class Barcharts: Basic bar chart, Grouped bar chart, Stacked bar chart.

    :return: No return.
    """
    # Basic bar chart

    # a = BarChart([3, 5, 9, 2, 6, 15], ['python', 'js', 'java', 'C', 'C++', 'Css'], 'Programming language usage', 'vertical')
    # a.basic_bar_chart('Usage')
    # plt.show()
    # # a.basic_bar_chart('Usage', 'Programming language usage', 'horizontal')
    # # plt.show()
    #
    # # Grouped bar chart
    # # list_x = [[3, 5, 9, 2, 6, 15], [20, 19, 35, 27, 16, 15], [23, 5, 13, 4, 20, 40]]
    # # c = BarChart(list_x, ['a', 'b', 'c', 'd', 'e', 'f'], 'test', 'vertical')
    # # c.multi_bar(['var1', 'var2', 'var3'], 'objects_test')
    # #
    # # Stacked bar chart
    list_x = [[3, 5, 9, 2, 6, 15], [20, 19, 35, 27, 16, 15], [23, 5, 13, 4, 20, 40]]
    c = BarChart(list_x, ['a', 'b', 'c', 'd', 'e', 'f'], 'test', 'horizontal')
    c.stacked_bar(['var1', 'var2', 'var3'])
    plt.show()

    # Boxplot
    # list_x1 = [[-0.46, -1.25, -2.62, 0.22], [0.24, 1.88, -0.49, -0.73, -0.49], [-0.44, 0.93, 0.19, -4.36, -0.88]]
    # d = BarChart(list_x1, ['G1', 'G2', 'G3'], 'Test', 'vertical')
    # d.box_plot('unit')
    # plt.show()
run_test()
