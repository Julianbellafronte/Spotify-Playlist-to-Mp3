import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout() #Creo una grilla de 3 columnas
        self.inside.cols = 3

        self.inside.add_widget(TextInput(text="Agrega el link aca")) #Creo textInput

        self.btnAdd = Button(text="Agregar") #Creo boton agregar
        self.btnAdd.bind(on_press=self.append)
        self.inside.add_widget(self.btnAdd)

        self.btnDownload = Button(text="Descargar") #Creo boton Descargar
        self.btnDownload.bind(on_press=self.download)
        self.inside.add_widget(self.btnDownload)

        self.add_widget(self.inside) #Agrego la grilla creada al main layout


    def append(self, instance):
        print("hola")
    
    def download(self, instance):
        print("chau")

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()