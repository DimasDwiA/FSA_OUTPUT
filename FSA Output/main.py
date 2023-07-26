from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase

from screens.screens import *

class WindowManager(ScreenManager):
    pass

class FSA(MDApp):
    CLASSES = {
        'Welcome' : 'screens.welcome'
    }
    AUTORELOADER_PATHS= [
        ('.', {'recursive' : True})
    ]
    KV_FILES = [
        'kv\welcome.kv'
    ]
    def build(self):
        self.wm = WindowManager()
        screens = [
            Home(name="home"),
            Balance(name="balance"),
            Size(name="size_pizza"),
            Flavor(name="flavor"),
            Summary(name="summary"),
            Ordering(name="ordering"),
            Diagram(name="diagram"),
            Diagram2(name="diagram2"),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == '__main__':
    LabelBase.register(name="timesnewroman", fn_regular="assets/Things/timesnewroman.ttf")
    LabelBase.register(name="timesnewroman_bold", fn_regular="assets/Things/timesnewroman_bold.ttf")
    LabelBase.register(name="Poppins-SemiBold", fn_regular="assets/Things/Poppins-SemiBold.ttf")
    LabelBase.register(name="Poppins-Bold", fn_regular="assets/Things/Poppins-Bold.ttf")
    LabelBase.register(name="Poppins-SemiBoldItalic", fn_regular="assets/Things/Poppins-SemiBoldItalic.ttf")
    FSA().run()
