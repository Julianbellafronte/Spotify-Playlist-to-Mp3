import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

# my app
class MyApp(GridLayout):
# layout
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs    )
        self.cols = 1 # Set columns for main layout

        layoutLinks = BoxLayout(padding=10, orientation='vertical')
        layoutTextbox = BoxLayout(padding=2, orientation='vertical')
        layoutBtn = BoxLayout(padding=2, orientation='vertical')

        self.inputs = GridLayout() # Create a new grid layout
        self.inputs.cols = 3 # set columns for the new grid layout

        self.btn1 = Button(text="Agregar")
        self.btn1.bind(on_press=self.buttonClickedAppend)

        self.btn2= Button(text="Descargar") 
        self.btn2.bind(on_press=self.buttonClickedDownload)
        
        self.inputs.add_widget(TextInput("Agrega el link aquí"))
        self.inputs.add_widget(self.btn1)
        self.inputs.add_widget(self.btn2)

        layoutTextbox.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=False)

# button click function
    def buttonClickedAppend(self,btn):
        print("agregado")

    def buttonClickedDownload(self,btn):
        print("descarga")

# run app
class MyApp(App):
    def build(self):
        return MyApp()


if __name__ == "__main__":
    MyApp().run()