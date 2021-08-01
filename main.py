from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button



class mainPage(GridLayout):
    next = "O"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    
    def click(self,n):
        n.text = self.next
        if self.next == "O":
            self.next = "X"
        else:
            self.next = "O"
        


class myApp(App):
    pass

myApp().run()