from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.audio import SoundLoader
import kivy

kivy.require("2.3.1")


class MenuApp(MDApp):
    """Main Application"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # load up title music and start it up
        self.title_music = SoundLoader.load("assets/sounds/music.mp3")
        self.play_music()
    def play_music(self, *args):
        if self.title_music and self.title_music.state == "stop":
            self.title_music.volume = 0.35
            self.title_music.loop = True
            self.title_music.play()
    def stop_music(self, *args):
        if self.title_music and self.title_music.state == "play":
            self.title_music.stop()
    def build(self):
        """Setup of the app"""
        # set default theme and colors
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        # register custom font
        LabelBase.register(
            name="jetbrains",
            fn_regular="assets/JetBrainsMono-Regular.ttf",
        )
        # change standard font to custom font
        self.theme_cls.font_styles.update({
            "H1": ["jetbrains", 90, True, 0.15],
            "H2": ["jetbrains", 60, False, -0.05],
            "H3": ["jetbrains", 48, False, 0],
            "H4": ["jetbrains", 34, False, 0.25],
            "H5": ["jetbrains", 24, False, 0],
            "H6": ["jetbrains", 20, False, 0.15],
            "Subtitle1": ["jetbrains", 16, False, 0.15],
            "Subtitle2": ["jetbrains", 14, False, 0.1],
            "Body1": ["jetbrains", 16, False, 0.5],
            "Body2": ["jetbrains", 14, False, 0.25],
            "Button": ["jetbrains", 14, True, 1.25],
            "Caption": ["jetbrains", 12, False, 0.4],
            "Overline": ["jetbrains", 10, True, 1.5],
        })
        # return the Manager instance as the root widget
        return Manager()


class Manager(MDScreenManager):
    """Class managing screen changes. If screen changes by a button declare on_release in kv file."""
    pass


class TitleScreen(MDScreen):
    """Title Screen"""
    pass


class SaveScreen(MDScreen):
    """Save states screen"""
    pass


class OptionsScreen(MDScreen):
    """Options screen"""
    pass


class GameScreen(MDScreen):
    """In-game screen"""
    pass


if __name__ == "__main__":
    MenuApp().run()