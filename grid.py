import pygame as py

class Grid:
    def __init__(self, width:int, height:int, rect_size:int,
                 line_width:int=1, corner_radius:int=0,
                 body_rgb:tuple[int, int, int]=(200, 200, 200),
                 line_rgb:tuple[int, int, int]=(50, 50, 50)):
        """
        Initializes a modular grid system.
        width: Grid width in pixels
        height: Grid height in pixels
        rect_size: Size of each grid cell in pixels
        line_width: Border thickness in pixels
        corner_radius: Rounded corner radius in pixels
        body_rgb: Cell color
        line_rgb: Grid line color
        """
        self.width = width
        self.height = height
        self.rect_size = rect_size
        self.line_width = line_width
        self.corner_radius = corner_radius
        self.body_rgb = body_rgb
        self.line_rgb = line_rgb
        self.cells = []
        self.surface = None  # Will be assigned during `set_surface`
        self.create_grid()

    def create_grid(self):
        """Generates the grid structure."""
        block_number = 1
        for y in range(self.height // self.rect_size):
            row= []
            for x in range(self.width // self.rect_size):
                rect = py.Rect(x * self.rect_size, y * self.rect_size,self.rect_size, self.rect_size)
                row.append({"rect": rect, "block_number": block_number,
                            "color": self.body_rgb, "corner_radius": self.corner_radius})
                #print(row) # debug
                block_number += 1
            self.cells.append(row)
            #print(self.cells) # debug

    def set_surface(self, surface):
        """Assigns a Pygame surface to draw on."""
        self.surface = surface

    def draw(self):
        """Draws the grid if a surface is set."""
        if self.surface:
            for row in self.cells:
                for cell in row:
                    corner_radius = cell["corner_radius"]
                    py.draw.rect(self.surface, cell["color"], cell["rect"], border_radius=corner_radius)
                    py.draw.rect(self.surface, self.line_rgb, cell["rect"], self.line_width, border_radius=self.corner_radius)

    def update_cell(self, x, y, primary_color = (255, 0, 0), secondary_color = (0, 255, 0)):
        """Updates a specific cell's color."""
        if 0 <= y < len(self.cells) and 0 <= x < len(self.cells[y]):
            self.cells[y][x]["color"] = primary_color
            self.cells[y][x]["corner_radius"] = self.corner_radius
            self.draw()

    def handle_events(self, event, primary_color = (255, 0, 0), secondary_color = (0, 255, 0)):
        """Handles mouse clicks to change cell colors interactively."""
        if event.type == py.MOUSEBUTTONUP:
            x, y = event.pos
            grid_x = x // self.rect_size
            grid_y = y // self.rect_size
            if 0 <= grid_y < len(self.cells) and 0 <= grid_x < len(self.cells[grid_y]):
                current_color = self.cells[grid_y][grid_x]["color"]
                new_color = secondary_color if current_color == primary_color else primary_color
                self.update_cell(grid_x, grid_y, new_color)
