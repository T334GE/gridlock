import pygame as py, sys

class Game:
    def __init__(self, screen):
        py.init()
        self.__screen = screen
        self.__screen_width = self.__screen.get_width()
        self.__screen_height = self.__screen.get_height()
        self.__font = py.font.Font("assets/fonts/JetBrainsMono-Regular.ttf", 60)
        self.__running:bool = True

    @property
    def is_running(self):
        return self.__running
    @is_running.setter
    def is_running(self, status:bool):
        self.__running = status

    def run(self):
        while self.__running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.__running = False
                    py.quit()
                    sys.exit()

            py.display.update()

if __name__ == "__main__":
    Game(
        screen=py.display.set_mode((1366,1024))
    ).run()