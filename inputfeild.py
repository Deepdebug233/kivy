from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Input(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',padding=150,spacing=35)

        self.Name = TextInput(text="Enter your name")
        self.Password = TextInput(text="Enter your password")
        self.sbmt =  Button(text="Submit",on_press=self.submit)

        layout.add_widget(self.Name)
        layout.add_widget(self.Password)
        layout.add_widget(self.sbmt)
        return layout
    def submit(self,obj):
        print(f"Your Name is ={self.Name.text}")
Input().run()


