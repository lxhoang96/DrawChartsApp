import pandas as pd
import matplotlib.pyplot as plt
from scatterchart import ScatterPlot


def test():
    # pd.set_option('display.float_format', lambda x: '%.2f' % x)
    gapminder = pd.read_csv('C:/Users/lxhoa/PycharmProjects/DrawChartsApp/gapminder.csv')
    print(gapminder.head())
    gapminder['oilperperson'] = pd.to_numeric(gapminder['oilperperson'], errors='coerce')
    gapminder['relectricperperson'] = pd.to_numeric(gapminder['relectricperperson'], errors='coerce')
    gapminder_clean = gapminder.dropna()
    # plt.figure()
    # sns.regplot(x='relectricperperson', y='oilperperson', fit_reg=True, data=gapminder_clean)
    chart = ScatterPlot('relectricperperson', 'oilperperson', 'Electrcity Use Per Person', 'Oil Use Per Person')
    chart.basic_scatter_plot(True, gapminder_clean)

    # plt.title('Scatterplot for the Association Between Electrcity Use Per Person' + '\n' + 'and Oil Use Per Person')
    plt.show()

test()