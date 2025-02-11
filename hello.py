from kivy.app import App
from kivy.uix.label import Label

class Deep(App):
    def build(self):
        return Label()
Deep().run()