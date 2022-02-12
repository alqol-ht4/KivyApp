from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
 

class MainTestApp(App):
    
    def build(self):
        return AsyncImage(source = "https://localhost/Projects/test.gif")
    
MainTestApp().run()
