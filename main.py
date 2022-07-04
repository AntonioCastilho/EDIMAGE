from editor import ed
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.clearcolor = .92, .92, .92, 1

bu = Builder.load_file('kvlang.kv')


class Programa(App):
    title = 'Check-in'

    def build(self):
        return bu


if __name__ == '__main__':
    Programa().run()
