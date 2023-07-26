from kivymd.uix.screen import MDScreen 
from kivy.lang import Builder
from kivy.properties import NumericProperty,StringProperty
from kivy.clock import Clock

class Summary(MDScreen):
    label_text = StringProperty("")
    text = StringProperty("")
    tulis = StringProperty("")
    price = StringProperty("")
    tax = StringProperty("")
    order = StringProperty("")
    time = StringProperty("")
    def __init__(self, **kw):
        Builder.load_file("kv/summary.kv")
        super().__init__(**kw)
    def cancel(self,*args):
        Clock.schedule_once(self.change_screen, 4)
        self.label_text = str("Sorry for the inconvenience, but with great regret, we decided to cancel your pizza order at this vending machine. Thank you for your understanding and patience. We hope to provide a better experience next time.")
    def change_screen(self, dt):
        self.label_text = str(" ")
        self.manager.current = "home"
    def update_text(self, new_text):
        self.text = new_text
    def update_flavor(self, new_tulis):
        self.tulis = new_tulis
    def update_price(self, new_price):
        self.price = new_price
    def update_tax(self, new_tax):
        self.tax = new_tax
    def update_order(self, new_order):
        self.order = new_order
    def update_time(self, new_time):
        self.time = new_time