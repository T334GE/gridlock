import pygame as py
from pygame.math import Vector2


class Player(py.sprite.Sprite):
    """Player class for turn based top down movement."""
    def __init__(self, radius: int, color: tuple[int, int, int], pos: Vector2, step_size: int = 100, grid=None):
        super().__init__()
        self.radius = radius
        self.color = color
        self.pos = pos
        self.step_size = step_size
        self.turn = True  # track if it's the player's turn
        self.grid = grid  # reference to the movement grid
        #self.current_cell = none
        self.image = py.Surface((self.radius * 2, self.radius * 2), py.SRCALPHA) # create player's image with transparency
        py.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=self.pos)# Set rect for positioning

    def handle_input(self):
        """Handle keyboard input for movement with turn-based control."""
        keys = py.key.get_pressed()
        moved = False
        up = Vector2(0, -1)
        down = Vector2(0, 1)
        left = Vector2(-1, 0)
        right = Vector2(1, 0)
        if keys[py.K_w]:
            self.move_to_cell(up)
            moved = True
        elif keys[py.K_s]:  # Down
            self.move_to_cell(down)
            moved = True
        elif keys[py.K_a]:  # Left
            self.move_to_cell(left)
            moved = True
        elif keys[py.K_d]:  # Right
            self.move_to_cell(right)
            moved = True
        if moved: self.turn = False  # end player's turn after moving
        self.rect.center = self.pos  # update rect position

    @property
    def current_cell(self): # without setter below this would be read only
        """Returns the rect object of the grid cell the player is currently in."""
        if self.grid is None: return None  # avoid NoneType errors
        grid_x = self.pos.x // self.grid.cell_size # determine the row via player position
        grid_y = self.pos.y // self.grid.cell_size
        if (0 <= grid_y < len(self.grid.cells) # checks if row is valid in index range
            and 0 <= grid_x < len(self.grid.cells[grid_y])): # check if column is valid
            return self.grid.cells[grid_y][grid_x]["rect"] # return rect object if all valid
        return None # in case if conditions fail

    def find_path(self, target_cell):
        """Find cells along a straight line from current cell to target cell.
        Returns a list of cell rects in the path (excluding current cell)."""
        path = []
        if not self.grid or not self.current_cell or not target_cell: return path
        start_pos = Vector2(self.current_cell.center)# get starting and ending points (center of cells)
        end_pos = Vector2(target_cell.center)
        direction = (end_pos - start_pos).normalize() # calculate direction vector and distance
        distance = start_pos.distance_to(end_pos)
        step_size = self.grid.cell_size / 4  # step through the line in small increments for better accuracy
        buffer = step_size * 0.1
        current_pos = start_pos.copy()
        while current_pos.distance_to(start_pos) <= distance + buffer:
            grid_x = int(current_pos.x // self.grid.cell_size)# convert to grid coordinates
            grid_y = int(current_pos.y // self.grid.cell_size)
            if (0 <= grid_y < len(self.grid.cells) # add cell to path if valid
                and 0 <= grid_x < len(self.grid.cells[grid_y])):
                cell_rect = self.grid.cells[grid_y][grid_x]["rect"]
                if cell_rect not in path:
                    path.append(cell_rect)
            current_pos += direction * step_size # move forward
        if target_cell not in path: path.append(target_cell) # force include target cell if missed
        return path

    def move_to_cell(self, direction: Vector2):
        """Move player to adjacent cell based on direction vector.
        Args:
            direction Vector2 with values like (0, -1) == (up), (1, 0) == (right), etc.
        """
        if not self.turn: return False
        target_pos = self.pos + (direction * self.step_size)# calculate target position
        grid_x = int(target_pos.x // self.grid.cell_size)# convert to grid coordinates
        grid_y = int(target_pos.y // self.grid.cell_size)
        if (0 <= grid_y < len(self.grid.cells)) and (0 <= grid_x < len(self.grid.cells[grid_y])): # check grid bounds
            self.pos = target_pos
            self.rect.center = self.pos  # update sprite position
            self.turn = False
            return True
        return False

    def update(self, surface):
        """Update player position and draw it on the screen."""
        self.rect.center = self.pos
        surface.blit(self.image, self.rect)

