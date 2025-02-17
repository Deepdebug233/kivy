from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class Manager(ScreenManager):
    pass
class MyApp(App):
    def build(self):
        pass
MyApp().run()