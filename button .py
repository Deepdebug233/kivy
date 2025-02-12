from kivy.app import App
from kivy.uix.button import Button

class Buttons(App):
    def build(self):
        return Button(text="Click me", size_hint=(0.2, 0.3), pos_hint={"x": 0.2, "y": 0.2})

Buttons().run()
