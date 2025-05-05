import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.core.window import Window
from kivy.core.text import FontContextManager as FCM
kivy.require("2.3.1")


class MenuApp(App):
    """Main Application"""
    def build(self):
        return Manager(transition=NoTransition())

class Manager(ScreenManager):
    """Class managing screen changes. All screens must be declared in grid.kv
    Name of the screen must be unique within a :class: `ScreenManager`.
    This is the name used for :attr: `ScreenManager.current`."""
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)

class TitleScreen(Screen):
    """Title Screen"""
    def __init__(self, **kwargs):
        super(TitleScreen, self).__init__(**kwargs)

class SaveScreen(Screen):
    """Save states screen"""
    def __init__(self, **kwargs):
        super(SaveScreen, self).__init__(**kwargs)

class OptionsScreen(Screen):
    """Options screen"""
    def __init__(self, **kwargs):
        super(OptionsScreen, self).__init__(**kwargs)

class GameScreen(Screen):
    """In-game screen"""
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_over)
    def on_mouse_over(self, window, pos):
        if self.collide_point(*pos):
            print(f"Collision at {pos}")






if __name__ == "__main__":
    MenuApp().run()