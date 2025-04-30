import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.core.audio import SoundLoader

kivy.require("2.3.1")


class MenuApp(App):
    """Main Application"""
    def build(self):
        m = Manager(transition=NoTransition())
        return m

class Manager(ScreenManager):
    """Class managing screen changes. All screens must be declared in grid.kv"""
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)

class TitleScreen(Screen):
    """Title Screen"""

class SaveScreen(Screen):
    """Save states screen"""

class OptionsScreen(Screen):
    """Options screen"""

if __name__ == "__main__":
    MenuApp().run()