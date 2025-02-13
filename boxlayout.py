from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BLayout(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',padding=50)
        btn1 = Button(text='Button1')
        btn2 = Button(text='Button2')
        btn3 = Button(text='Button3')
        btn4 = Button(text='Button4')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout
BLayout().run()