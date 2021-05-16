from scrapper import Main
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainBox(BoxLayout):
    pass

class Box(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        elements = Main.build()
        for element in elements:
            self.add_widget(Movies(text=element))

class Movies(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text


class Interface(App):
    def build(self):
        return MainBox()


Interface().run()
