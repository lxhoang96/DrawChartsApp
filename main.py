# from linechart import LineChart
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.core.window import Window
Chart_list = ['Area chart', 'Bar chart', 'Box plot', 'Bubble chart', 'Histogram', 'Line chart', 'Pie chart', 'Radar chart', 'Scatter chart']


class DrawChartsApp(App):
    """

    """
    Chart_list = ListProperty()

    def __init__(self, **kwargs):
        super(DrawChartsApp, self).__init__(**kwargs)

        self.list_chart = Chart_list
        self.first_chart = self.list_chart[0]

    def build(self):
        """

        :return:
        """
        # Window.clearcolor = (1, 1, 1, 1)
        # Window.size = (700, 1300)
        self.title = 'Draw chart App'
        self.root = Builder.load_file('app.kv')

        return self.root

    # def draw_charts(self, key):
        # if str(key) == self.list_chart[0]:



if __name__ == '__main__':
    DrawChartsApp().run()
