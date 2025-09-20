import pygame as py

class Map:
    def __init__(self, screen:py.Surface, rows:int, columns:int):
        self.rows = rows
        self.columns = columns
        self.screen = screen
        self.cell_width = self.screen.get_width() // self.rows
        self.cell_height = self.screen.get_width() // self.columns

    def draw(self):
        for row in range(self.rows):
            for col in range(self.columns):
                rect = py.Rect(
                    col * self.cell_width,
                    row * self.cell_height,
                    self.cell_width,
                    self.cell_height,
                )
                py.draw.rect(self.screen, (200, 200, 200), rect, 1)