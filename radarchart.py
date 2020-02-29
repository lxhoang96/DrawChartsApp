import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import numpy as np


class RadarChart:

    def __init__(self, data=None):
        self.data = data

    def basic_radar_chart(self):

        df = pd.DataFrame(self.data)
        categories = list(df)[1:]
        N = len(categories)
        values = df.loc[0].drop(str(list(df)[0])).values.flatten().tolist()
        values += values[:1]

        angles = [n / float(N)*2*pi for n in range(N)]
        angles += angles[:1]

        ax = plt.subplot(111, polar=True)

        max_each = df.max(axis=1)
        result = []
        for i in range(len(max_each)):
            result.append(max_each.get(key=i))
        int_result = np.array(result, dtype=np.int)
        list_value = []
        for i in range(0, max(int_result)):
            if i % 10 == 0:
                list_value.append(i)

        plt.xticks(angles[:-1], categories, color='grey', size=8)
        ax.set_rlabel_position(0)

        plt.yticks(list_value, list(map(str, list_value)), color='grey', size=7)
        plt.ylim(0, max(list_value)+10)

        ax.plot(angles, values, linewidth=1, linestyle='solid')

        ax.fill(angles, values, 'b', alpha=0.1)



