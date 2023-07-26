from kivymd.uix.screen import MDScreen 
from kivy.lang import Builder
from kivy.properties import NumericProperty,StringProperty

class Flavor(MDScreen):
    label_text = StringProperty()
    def __init__(self, **kw):
        Builder.load_file("kv/flavor.kv")
        super().__init__(**kw)
    def on_flavor_button_click(self, flavor):
        summary_screen = self.manager.get_screen("summary")
        summary_screen.update_flavor(flavor)
        self.manager.current = "summary"
    def on_pricer_button_click(self, price):
        summary_screen = self.manager.get_screen("summary")
        summary_screen.update_price(price)
    def on_tax_button_click(self, tax):
        summary_screen = self.manager.get_screen("summary")
        summary_screen.update_tax(tax)
    def on_time_button_click(self, time):
        summary_screen = self.manager.get_screen("summary")
        summary_screen.update_time(time)