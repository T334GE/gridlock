from scripts.App import GameApp

class Main:
    """Main entry point for the application."""
    def __init__(self):
        self.__app = GameApp()
    @property
    def app(self):
        """Returns the GameApp instance."""
        return self.__app


if __name__ == "__main__":
    Main().app.run()