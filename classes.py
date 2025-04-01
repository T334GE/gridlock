import pygame as py
from pygame import Vector2

vec = py.math.Vector2

class Player(py.sprite.Sprite):
    def __init__(self, width: int, height: int, color: tuple[int, int, int], pos: Vector2):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.pos = Vector2(pos)
        # Create the player's image and draw the circle
        self.image = py.Surface((self.width * 2, self.height * 2), py.SRCALPHA)  # Ensure transparency
        py.draw.circle(self.image, self.color, (self.width, self.height), self.width)  # Draw centered circle
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, surface):
        self.rect.center = self.pos  # Update rect position based on `pos`
        surface.blit(self.image, self.rect)  # Draw player on surface
