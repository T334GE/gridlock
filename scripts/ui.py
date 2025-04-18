import pygame.freetype as freetype
from pygame.sprite import Sprite


def create_surface_with_text(text, font_size:int or float, text_rgb:tuple[int, int, int], bg_rgb:tuple[int, int, int]):
    font = freetype.SysFont("JetBrains Mono Regular", font_size, bold = True)
    surface, _ = font.render(text = text, fgcolor= text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class Text_Button(Sprite):
    def __init__(self, center_position:tuple[int, int], text:str, font_size:int or float,
                 bg_rgb, text_rgb:tuple[int, int, int],text_highlight_rgb:tuple[int, int, int], action=None):
        """ An user interface element that can be added to a surface.
            bg_rgb can be tuple[int, int, int] or False for transparent background
        """
        self.mouse_over = False
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb)
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_highlight_rgb, bg_rgb=bg_rgb)
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position)]
        self.action = action
        super().__init__()

    @property
    def image(self): return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self): return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up: return self.action
        else:
            if self.mouse_over: self.mouse_over = False
        return None

    def draw(self, surface):
        surface.blit(self.image, self.rect)

