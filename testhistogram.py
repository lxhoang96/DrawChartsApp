from histogram import Histogram
import matplotlib.pylab as plt
import pandas as pd


def test():
    gapminder = pd.read_csv('C:/Users/lxhoa/PycharmProjects/DrawChartsApp/gapminder.csv')
    print(gapminder.head())
    gapminder['oilperperson'] = pd.to_numeric(gapminder['oilperperson'], errors='coerce')
    gapminder['relectricperperson'] = pd.to_numeric(gapminder['relectricperperson'], errors='coerce')
    gapminder_clean = gapminder.dropna()
    chart = Histogram(gapminder_clean['relectricperperson'])
    chart.basic_histogram(xname='reelectricperperson', title='Total electric per person')

    # plt.title('Scatterplot for the Association Between Electrcity Use Per Person' + '\n' + 'and Oil Use Per Person')
    plt.show()


test()