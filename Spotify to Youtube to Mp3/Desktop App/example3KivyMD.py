from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivymd.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        self.btnAdd = Button(text="Agregar",size_hint_x=None, width=100, height=100) #Creo boton agregar
        gridlayout = GridLayout(row_force_default=True, row_default_height=40, cols=3)
        self.btnAdd1 = Button(text="Agregar",size_hint_x=None, width=100, height=100) #Creo boton agregar

        # Creating a Simple List
        scroll = ScrollView()

        list_view = MDList()

        items = OneLineListItem(text=str("1") + ' item')
        list_view.add_widget(items)

        scroll.add_widget(list_view)
        gridlayout.add_widget(self.btnAdd)
        

        # End List

        screen.add_widget(scroll)
        screen.add_widget(gridlayout)
        return screen





DemoApp().run()