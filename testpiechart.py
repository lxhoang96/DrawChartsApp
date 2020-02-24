from piecharts import PieCharts
import matplotlib.pylab as plt


def test_pie_chart():
    labels = ['Apple', 'Orange', 'Lemon', 'Grapes', 'Durian', 'Peach']
    sizes = [15, 20, 5, 10, 7, 8]
    fruit = PieCharts(labels, sizes)
    fruit.basic_pie_chart('Kind of fruits', 'kg')
    plt.show()


test_pie_chart()
