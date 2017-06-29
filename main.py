from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.core.window import WindowBase
from exp1 import test as t1
import os
from exp2 import test2 as t2
#from exp3 import test2 as t3
#from exp4 import test as t4
#from exp5 import test as t5
#from exp6 import test as t6
#Window.fullscreen = 'fake'
Window.clearcolor = (0.1, 0.1, 0.1, 1)
from kivy.config import Config
Config.set('graphics','resizable',0)
from kivy.core.window import Window
Window.size = (1280, 720)

class SiplabApp(App):
    def siplab(self,s):
        App.get_running_app().stop()
        if(s=="exp1"):
            os.chdir("./exp1/")
            print(os.getcwd())
            t1.SimulatorApp().run()
        elif(s=="exp2"):
            os.chdir("./exp2/")
            print(os.getcwd())
            t2.SimulatorApp().run()
        elif(s=="exp4"):
            os.chdir("./exp4/")
            print(os.getcwd())
            t4.betaApp().run()
        elif(s=="exp5"):
            os.chdir("./exp5/")
            print(os.getcwd())
            t5.SimulatorApp().run()
        elif(s=="exp6"):
            os.chdir("./exp6/")
            print(os.getcwd())
            t6.BetaApp().run()

SiplabApp().run()