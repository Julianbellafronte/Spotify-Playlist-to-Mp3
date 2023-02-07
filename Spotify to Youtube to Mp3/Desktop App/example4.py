import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        Builder.load_file("medium.kv")

        Window.clearcolor = (0.2, 0.1, 0.30, 1)

        self.cols = 1

        self.gridMain = GridLayout(row_force_default=True, row_default_height=80) #Creo una grilla de 3 columnas (input, btnAgregar, btnDescargar)
        self.gridMain.cols = 1

        self.gridInput = GridLayout(row_force_default=True, row_default_height=40) #Creo una grilla de 3 columnas (input, btnAgregar, btnDescargar)
        self.gridInput.cols = 3

        self.gridLinks = GridLayout(row_force_default=True, row_default_height=40) #Creo una grilla de 1 columna (links)
        self.gridLinks.cols = 1

        self.textbox = TextInput()
        self.gridInput.add_widget(self.textbox) #Creo textInput

        self.btnAdd = Button(text="Agregar",size_hint_x=None, width=100, height=100) #Creo boton agregar
        self.btnAdd.bind(on_press=self.append)
        self.gridInput.add_widget(self.btnAdd)

        self.btnDownload = Button(text="Descargar") #Creo boton Descargar
        self.btnDownload.bind(on_press=self.download)
        self.gridInput.add_widget(self.btnDownload)


        self.gridMain.add_widget(self.gridInput)
        self.gridMain.add_widget(self.gridLinks)

        self.add_widget(self.gridMain) #Agrego la grilla creada al main layout

    def append(self, instance):
        print(self.textbox.text)
        self.gridLinks.add_widget(Label(text=self.textbox.text))
    
    def download(self, instance):
        print("chau")

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()