import matplotlib.pylab as plt
from bubblechart import BubbleChart
import pandas as pd


def test():
    gapminder = pd.read_csv('gapminder.csv')
    # gapminder = pd.read_csv('C:/Users/lxhoa/PycharmProjects/DrawChartsApp/gapminder.csv')
    print(gapminder.head())
    gapminder['oilperperson'] = pd.to_numeric(gapminder['oilperperson'], errors='coerce')
    gapminder['relectricperperson'] = pd.to_numeric(gapminder['relectricperperson'], errors='coerce')
    gapminder_clean = gapminder.dropna()
    list_x = [gapminder_clean['oilperperson'], gapminder_clean['relectricperperson']]
    c = BubbleChart(list_x)
    c.basic_bubble(True, 'circle', [[6, 0], [0, 6000]])
    plt.show()

test()
