import matplotlib.pylab as plt
from areacharts import AreaCharts


def test():
    labels = ['Chairs', 'Desks', 'Tables', 'TV']
    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
    values = [[3, 5, 9, 2, 6, 15], [20, 19, 35, 27, 16, 15], [23, 5, 13, 4, 20, 40], [3, 5, 9, 7, 20, 6]]
    test1 = AreaCharts(month, values)
    test1.basic_chart(labels, 'upper left')
    plt.show()


test()
