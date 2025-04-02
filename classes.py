import pygame as py
from pygame.math import Vector2


class Player(py.sprite.Sprite):
    """Player class for turn based top down movement."""
    def __init__(self, radius: int, color: tuple[int, int, int], pos: Vector2, step_size: int = 100, grid=None):
        super().__init__()
        self.radius = radius
        self.color = color
        self.pos = Vector2(pos)
        self.step_size = step_size
        self.turn = True  # Track if it's the player's turn
        self.grid = grid  # Reference to the movement grid
        #self.current_cell = None
        self.image = py.Surface((self.radius * 2, self.radius * 2), py.SRCALPHA)# Create player's image with transparency
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
        if moved: self.turn = False  # End player's turn after moving
        self.rect.center = self.pos  # Update rect position

    @property
    def current_cell(self): # without setter below this would be read only
        """Returns the rect object of the grid cell the player is currently in."""
        if self.grid is None: return None  # Avoid NoneType errors
        grid_x = self.pos.x // self.grid.cell_size # determine the row via player position
        grid_y = self.pos.y // self.grid.cell_size
        if (0 <= grid_y < len(self.grid.cells) # checks if row is valid in index range
            and 0 <= grid_x < len(self.grid.cells[grid_y])): # check if column is valid
            return self.grid.cells[grid_y][grid_x]["rect"] # return rect object if all valid
        return None # in case if conditions fail

    def find_path(self, target_cell):
        """A* pathfinding implementation."""
        if not self.grid or not self.current_cell: return []

    def move_to_cell(self, direction: Vector2):
        """Move player to adjacent cell based on direction vector.
        Args:
            direction: Vector2 with values like (0, -1) == (up), (1, 0) == (right), etc.
        """
        if not self.turn: return False
        target_pos = self.pos + (direction * self.step_size)# Calculate target position
        grid_x = int(target_pos.x // self.grid.cell_size)# Convert to grid coordinates
        grid_y = int(target_pos.y // self.grid.cell_size)
        # Check grid bounds
        if (0 <= grid_y < len(self.grid.cells)) and (0 <= grid_x < len(self.grid.cells[grid_y])):
            self.pos = target_pos
            self.rect.center = self.pos  # Update sprite position
            self.turn = False
            return True
        return False
    def update(self, surface):
        """Update player position and draw it on the screen."""
        self.rect.center = self.pos
        surface.blit(self.image, self.rect)

