import pygame as py
from pygame import Vector2

class Platform(py.sprite.Sprite):
    def __init__(
            self,
            pos:Vector2|tuple[int,int],
            size:Vector2|tuple[int,int] = Vector2(100,30),
            color:tuple[int,int,int] = (200,200,200),
            vel:Vector2|tuple[int,int] = Vector2(0,0),
            acc:Vector2|tuple[int,int] = Vector2(0,0)
        ):
        super().__init__()
        self.size = size
        self.color = color
        self.image = py.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.update()

    def update(self, *args, **kwargs) -> None:
        self.vel += self.acc
        self.pos += self.vel
        self.rect.topleft = self.pos
        print(self.pos)
