from kivymd.uix.screen import MDScreen  
from kivy.lang import Builder
from kivy.properties import NumericProperty,StringProperty
from kivy.clock import Clock

class Balance(MDScreen):
    label_text = StringProperty()
    def __init__(self, **kw):
        Builder.load_file("kv/balance.kv")
        super().__init__(**kw)
        self.count = 0
        self.label_text = str(self.count)
    def limapuluh(self,*args):
        self.count = 50000
        Clock.schedule_once(self.change_screen, 2)
        self.label_text = str(self.count)
    def seratus(self,*args):
        self.count = 100000
        Clock.schedule_once(self.change_screen, 2)
        self.label_text = str(self.count)
    def seratuslimapuluh(self,*args):
        self.count = 150000
        Clock.schedule_once(self.change_screen, 3)
        self.label_text = str(self.count)
    def change_screen(self, dt):
        self.count = 0
        self.label_text = str(self.count)
        self.manager.current = "size_pizza"

        