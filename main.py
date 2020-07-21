import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button   
kivy.require('1.9.0')   
      
# to change the kivy default settings we use this module config  
from kivy.config import Config
      
# 0 being off 1 being on as in true / false  
# you can use 0 or 1 && True or False  
Config.set('graphics', 'resizable', True)
Config.set('kivy','window_icon','images/hqdefault.ico')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.scrollview import ScrollView
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty

Builder.load_file('design.kv')

class InitialScreen(Screen):

    sound = ObjectProperty(None, allownone=True)

    def play(self, filename):
        if self.sound is None:
            path = ('sounds/{}.wav'.format(filename))
            self.sound = SoundLoader.load(path)
        #stop sound if it's playing
        if self.sound.status != 'stop':
            self.sound.stop()
        self.sound.play()




class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()