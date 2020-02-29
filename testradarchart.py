import matplotlib.pylab as plt
from radarchart import RadarChart


def test():
    list_x = {
'group': ['A','B','C','D'],
'var1': [38, 1.5, 30, 4],
'var2': [29, 10, 9, 34],
'var3': [8, 39, 23, 24],
'var4': [7, 31, 33, 14],
'var5': [28, 15, 32, 14]
}
    c = RadarChart(list_x)
    c.basic_radar_chart()
    plt.show()

test()