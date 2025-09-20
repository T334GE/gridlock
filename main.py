from scripts.classes.Game import *

if __name__ == "__main__":
    Game(
        screen=py.display.set_mode((1366,1024),py.RESIZABLE)
    ).run()