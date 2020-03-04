from linechart import LineChart
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.core.window import Window

class DrawChartsApp(App):
    """

    """
    def __init__(self, **kwargs):
        super(DrawChartsApp, self).__init__(**kwargs)

    def build(self):
        """

        :return:
        """
        self.title = 'Draw chart App'
        self.root = Builder.load_file('app.kv')
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (700, 1300)
        return self.root


myApp = DrawChartsApp()
myApp.run()
