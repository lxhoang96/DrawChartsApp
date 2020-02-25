import matplotlib.pylab as plt
import numpy as np


class PieCharts:

    def __init__(self, labels=None, sizes=None, explode=None):
        self.labels = labels
        self.sizes = sizes
        self.explode = explode

    def basic_pie_chart(self, title='', units=''):
        fig, ax = plt.subplots()

        wedges, texts, autotexts = ax.pie(self.sizes, explode=self.explode, labels=self.labels, autopct='%1.1f%%', startangle=90, textprops=dict(color='w'))
        ax.legend(wedges,  self.labels, title='Unit: {}'.format(units), loc='upper right')
        plt.setp(autotexts, size=8, weight='bold')
        ax.set_title(title, size=12)
        ax.axis('equal')

    def donut_chart(self):
        fig, ax = plt.subplots()
        wedges, texts = ax.pie(self.sizes, explode=self.explode, wedgeprops=dict(width=0.5), startangle=90)
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"),
                  bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1) / 2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontal_alignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connection_style = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connection_style})
            ax.annotate(self.labels[i], xy=(x, y), xytext=(1.2 * np.sign(x), 1.4 * y),
                        horizontalalignment=horizontal_alignment, **kw)
