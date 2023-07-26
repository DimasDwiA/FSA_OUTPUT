from kivymd.uix.screen import MDScreen 
from kivy.lang import Builder
from kivy.properties import NumericProperty,StringProperty
from kivy.clock import Clock

class Size(MDScreen):
    label_text = StringProperty("")
    size_text = StringProperty()
    def __init__(self, **kw):
        Builder.load_file("kv/size_pizza.kv")
        super().__init__(**kw)
    def on_size_button_click(self, size):
        summary_screen = self.manager.get_screen("summary")
        summary_screen.update_text(size)
        self.manager.current = "flavor"
    def on_order_button_click(self, size):
        summary_screen = self.manager.get_screen("summary")
        summary_screen.update_order(size)