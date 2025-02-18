from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
class Page(App):
    def build(self):
        
        layout= PageLayout()
        btn1=Button(text="FirstButton",size_hint=(None,None),width=100)
        btn2=Button(text="NextButton",size_hint=(None,None),width=100)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout

Page().run()