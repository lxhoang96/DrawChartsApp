from linechart import LineChart
import matplotlib.pylab as plt


def run_test():
    a = LineChart([1, 3, 4, 8], [5, 10, 15, 30])
    b = LineChart([1, 3, 4, 8], [10, 15, 20, 23])
    c = LineChart([1, 3, 4, 8], [3, 6, 7, 10])
    a.basic_line_chart('month', 'money')
    plt.show()
    a.basic_line_chart()
    b.basic_line_chart()
    c.basic_line_chart()
    plt.show()

    # list1 = [a, b, c]
    # draw1 = list1.multi_line_chart()
    # plt.show()


run_test()
