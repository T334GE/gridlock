import pygame as py, sys, pygame_gui as pygui

class Game:
    def __init__(self, screen):
        py.init()
        self.__screen = screen
        self.__screen_width = self.__screen.get_width()
        self.__screen_height = self.__screen.get_height()
        self.__screen_size = self.__screen_width, self.__screen_height
        self.__background = py.Surface(self.__screen_size)

        self.__font = py.font.Font("assets/fonts/JetBrainsMono-Regular.ttf", 60)
        self.__manager = pygui.UIManager(self.__screen_size, theme_path="scripts/theme.json")
        self.__clock = py.time.Clock()
        self.__time_delta = None

        self.__is_running:bool = True

        self.__menu_container = pygui.elements.UIPanel(
            py.Rect(-1, -1, 200, 500),
            anchors={"center":"center"},
            object_id="main_menu_container"
        )
        self.__start_button = pygui.elements.UIButton(
            py.Rect(-1, 50, 75, -1),
            text="start",
            anchors={"centerx":"centerx",
                     "bottom_target": "self.__exit_button"},
            container=self.__menu_container,
            object_id="start_btn"
        )
        self.__exit_button = pygui.elements.UIButton(
            py.Rect(-1, 100, 75, -1),
            text="exit",
            anchors={"centerx":"centerx",
                     "top_target": "self.__start_button"},
            container=self.__menu_container,
            object_id="exit_btn"
        )



    @property
    def is_running(self) -> bool:
        return self.__is_running
    @is_running.setter
    def is_running(self, status:bool):
        self.__is_running = status


    def run(self):
        while self.__is_running:
            self.__time_delta = self.__clock.tick(60)/1000.0
            for event in py.event.get():
                match event.type:
                    case py.QUIT:
                        self.__is_running = False

                    case pygui.UI_BUTTON_PRESSED:
                        if event.ui_element.text == "exit":
                            self.__is_running = False

                    case py.VIDEORESIZE:
                        self.__screen = py.display.set_mode((event.w, event.h),py.RESIZABLE)
                        self.__manager.set_window_resolution((event.w, event.h))
                        self.__menu_container.update(self.__time_delta)

                self.__manager.process_events(event)

            self.__manager.update(self.__time_delta)
            self.__screen.fill((0,0,0))
            self.__manager.draw_ui(self.__screen)

            py.display.flip()

if __name__ == "__main__":
    Game(
        screen=py.display.set_mode((1366,1024),py.RESIZABLE)
    ).run()