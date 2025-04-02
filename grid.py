import pygame as py


class Grid:
    def __init__(
            self, surface, width:int, height:int, cell_size:int,
            line_width:int=1,corner_radius=10,
            body_rgb:tuple[int, int, int]=(200, 200, 200),
            line_rgb:tuple[int, int, int]=(50, 50, 50)):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.line_width = line_width
        self.corner_radius = corner_radius
        self.body_rgb = body_rgb
        self.line_rgb = line_rgb
        self.cells = []
        self.surface = surface
        self.create_grid()

    def create_grid(self):
        """Generates the grid structure and saves all cells in a dict."""
        cell_number = 1
        for y in range(self.height // self.cell_size):
            row = []
            for x in range(self.width // self.cell_size):
                cell = py.Rect(x * self.cell_size, y * self.cell_size,
                               self.cell_size, self.cell_size)
                row.append({
                    "cell_number": cell_number,
                    "rect": cell,
                    "color": self.body_rgb,
                    "corner_radius": self.corner_radius
                })
                cell_number += 1
            self.cells.append(row)

    def draw(self):
        """Draws the entire grid (used initially)."""
        if self.surface:
            for row in self.cells:
                for cell in row:
                    self.draw_cell(cell)

    def draw_cell(self, cell):
        """Draws an individual cell."""
        if self.surface:
            py.draw.rect(self.surface, cell["color"], cell["rect"],
                         border_radius=cell["corner_radius"])
            py.draw.rect(self.surface, self.line_rgb, cell["rect"],
                         self.line_width, border_radius=self.corner_radius)

    def get_cell(self, cell_rect):
        """Finds a cell dictionary using its Rect object.
           Returns the cell dictionary if found, otherwise returns None."""
        for row in self.cells:
            for cell in row:
                if cell["rect"] == cell_rect:
                    return cell
        return None

    def get_this_cell(self, position:tuple[int, int]):
        """Returns the cell on parsed position.
           Returns None if no cell."""
        for row in self.cells:
            for cell in row:
                if cell["rect"].collidepoint(position):
                    return cell
        return None

    def toggle_cell_color(self, cell_rect, primary_color=(0, 0, 0),secondary_color=(20, 100, 20)):
        """Toggles the color of a cell and redraws only that cell."""
        cell = self.get_cell(cell_rect)
        if cell:
            current_color = cell["color"]
            cell["color"] = (secondary_color
                             if current_color == primary_color
                             else primary_color)
            self.draw_cell(cell)
            py.display.update(cell["rect"])
