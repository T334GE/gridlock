import pygame as py, pygame_gui as pygui
from scripts.classes.Entities import Platform
from scripts.classes.UI import UI
from scripts.classes.Map import Map

class Game:
    def __init__(self, screen:py.Surface):
        py.init()
        self.screen:py.Surface = screen
        self.screen_width:int = self.screen.get_width()
        self.screen_height:int = self.screen.get_height()
        self.screen_size:tuple[int,int] = self.screen_width, self.screen_height
        self.background = py.Surface(self.screen_size)  # temporary
        self.font = py.font.Font("./assets/fonts/JetBrainsMono-Regular.ttf", 60)

        self.manager:pygui.UIManager = pygui.UIManager(self.screen_size, theme_path="scripts/theme.json")
        self.ui:UI = UI(self.manager)
        self.map:Map = Map(self.screen, 8, 8)
        self.clock:py.time.Clock = py.time.Clock()
        self.time_delta = None
        self.is_running:bool = True
        self.is_paused:bool  = False
        self.game_state:str = "title_screen"

    def run(self) -> None:
        all_sprites:py.sprite.Group = py.sprite.Group()
        while self.is_running:
            self.time_delta = self.clock.tick(60) / 1000.0
            for event in py.event.get():
                match event.type:
                    case py.QUIT:
                        self.is_running = False
                    case pygui.UI_BUTTON_PRESSED:  # all ui events in this case
                        match event.ui_element.text:
                            case "exit":
                                if self.game_state is None:
                                    self.is_running = False
                                elif not self.game_state is None:
                                    self.game_state = None
                            case "start":
                                self.game_state = 1
                    case py.KEYDOWN:  # all key events in this case
                        if event.key == py.K_d:
                            if not self.manager.visual_debug_active:
                                self.manager.set_visual_debug_mode(True)
                            else:
                                self.manager.set_visual_debug_mode(False)
                        if event.key == py.K_ESCAPE:
                            match self.game_state:
                                case None:
                                    self.is_running = not self.is_running
                                case 1:
                                    self.is_paused = not self.is_paused
                        if event.key == py.K_s:
                            PL1:Platform = Platform(py.mouse.get_pos())
                            all_sprites.add(PL1)
                    case py.VIDEORESIZE:
                        self.screen = py.display.set_mode((event.w, event.h), py.RESIZABLE)
                        self.manager.set_window_resolution((event.w, event.h))
                        self.map = Map(self.screen, 8, 8)

                self.manager.process_events(event)
                print(event)


            self.manager.update(self.time_delta)
            self.screen.fill((0, 0, 0))
            if self.game_state == 1:
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

