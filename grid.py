import pygame as py


class Grid:
    def __init__(self,surface, width, height, cell_size, line_width=1, corner_radius=0,
                 body_rgb=(200, 200, 200), line_rgb=(50, 50, 50)):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.line_width = line_width
        self.corner_radius = corner_radius
        self.body_rgb = body_rgb
        self.line_rgb = line_rgb
        self.cells = []
        self.surface = surface  # Will be assigned during `set_surface`
        self.create_grid()

    def create_grid(self):
        """Generates the grid structure."""
        cell_number = 1
        for y in range(self.height // self.cell_size):
            row = []
            for x in range(self.width // self.cell_size):
                cell = py.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                row.append({"cell": cell, "cell_number": cell_number,
                            "color": self.body_rgb, "corner_radius": self.corner_radius})
                cell_number += 1
            self.cells.append(row)


    def draw(self):
        """Draws the grid if a surface is set."""
        if self.surface:
            for row in self.cells:
                for cell in row:
                    corner_radius = cell["corner_radius"]
                    py.draw.rect(self.surface, cell["color"], cell["cell"], border_radius=corner_radius)
                    py.draw.rect(self.surface, self.line_rgb, cell["cell"], self.line_width,
                                 border_radius=self.corner_radius)

    def get_info(self, event):
        """Handles events and returns the block number and (x, y) position of the cell."""
        x, y = event.pos
        grid_x = x // self.cell_size
        grid_y = y // self.cell_size

        if 0 <= grid_y < len(self.cells) and 0 <= grid_x < len(self.cells[grid_y]):
            event_cell = self.cells[grid_y][grid_x]  # Get the entire cell dictionary
            cell_x, cell_y = event_cell["cell"].topleft  # Exact position of the cell
            cell_number = event_cell["cell_number"]
            return {"cell_number": cell_number, "x": cell_x, "y": cell_y}
        return None  # If out of bounds, return None

    def on_cell(self, cell_number):
        """Finds a cell dictionary using its block number.
            returns Boolean on index 0, cell dict on 1."""
        for row in self.cells:
            for cell in row:
                if cell["cell_number"] == cell_number:
                    return True, cell
        return False  # Return False if not found

    def toggle_cell_color(self, cell_number, primary_color=(0, 0, 0), secondary_color=(255, 0, 0)):
        """Toggles the color of the cell based on its block number."""
        cell = self.on_cell(cell_number)
        if cell:
            current_color = cell[1]["color"]
            new_color = secondary_color if current_color == primary_color else primary_color
            cell[1]["color"] = new_color
            self.draw()  # Re-draw the grid with the updated color

