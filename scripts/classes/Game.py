import pygame as py, pygame_gui as pygui
from scripts.classes.Entities import Platform
from scripts.classes.UI import UI
from scripts.classes.Map import Map

class Game:
    def __init__(self, screen:py.Surface):
        py.init()
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.screen_size = self.screen_width, self.screen_height
        self.background = py.Surface(self.screen_size)  # temporary
        self.font = py.font.Font("./assets/fonts/JetBrainsMono-Regular.ttf", 60)

        self.manager = pygui.UIManager(self.screen_size, theme_path="scripts/theme.json")
        self.ui = UI(self.manager)
        self.map = Map(self.screen, 8, 8)
        self.clock = py.time.Clock()
        self.time_delta = None
        self.is_running:bool = True
        self.is_paused:bool  = False
        self.game_state:str|None = None

    def run(self) -> None:
        all_sprites = py.sprite.Group()
        while self.is_running:
            self.time_delta = self.clock.tick(60) / 1000.0
            for event in py.event.get():
                match event.type:
                    case py.QUIT:
                        self.is_running = False

                    case pygui.UI_BUTTON_PRESSED:  # all ui events in this case
                        if event.ui_element.text == "exit":
                            self.is_running = False
                        if event.ui_element.text == "start":
                            self.game_state = "l1"


                    case py.KEYDOWN:  # all key events in this case
                        if event.key == py.K_d:
                            if not self.manager.visual_debug_active:
                                self.manager.set_visual_debug_mode(True)
                            else:
                                self.manager.set_visual_debug_mode(False)
                        if event.key == py.K_ESCAPE:
                            if self.game_state is None:
                                self.is_running = False
                            elif self.game_state:
                                self.game_state = None
                            else:
                                if not self.is_paused:
                                    self.is_paused = True
                                else:
                                    self.is_paused = False


                        if event.key == py.K_s:
                            PL1 = Platform(py.mouse.get_pos())
                            all_sprites.add(PL1)

                    case py.VIDEORESIZE:
                        self.screen = py.display.set_mode((event.w, event.h), py.RESIZABLE)
                        self.manager.set_window_resolution((event.w, event.h))
                        self.map = Map(self.screen, 8, 8)

                self.manager.process_events(event)
                print(event)


            self.manager.update(self.time_delta)
            self.screen.fill((0, 0, 0))
            if self.game_state == "l1":
                self.ui.menu_container.disable()
                self.ui.menu_container.hide()
                self.map.draw()
            if self.is_paused or self.game_state is None:
                self.ui.menu_container.enable()
                self.ui.menu_container.show()
            self.manager.draw_ui(self.screen)
            all_sprites.update()
            all_sprites.draw(self.screen)

            py.display.flip()

