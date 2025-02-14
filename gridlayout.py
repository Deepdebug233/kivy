from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class BLayout(App):
    def build(self):
        layout = GridLayout(cols=2,row_force_default=True,row_default_height=50)
        btn1 = Button(text='Button1')
        btn2 = Button(text='Button2')
        btn3 = Button(text='Button3')
        btn4 = Button(text='Button4')
        btn5 = Button(text='Button5')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)

        return layout
BLayout().run()