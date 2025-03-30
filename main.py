import pygame, pygame.freetype, pyglet, sys, time, random
from enum import Enum
from pygame.sprite import Sprite
from pygame.sprite import RenderUpdates

COLORS = {
    "black": (0, 0, 0),
    "brown": (165, 60, 60),
    "gray": (120, 120, 120),
    "white": (255, 255, 255),
    "red": (100, 0, 0),
    "green": (0, 100, 0),
    "blue": (0, 0, 100),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255)
}

width, height = 1000, 1000
size = (width, height)
screen = pygame.display.set_mode(size)
block_size:int = 100
clock = pygame.time.Clock()

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("JetBrains Mono Regular", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    def __init__(
            self,
            center_position:tuple[float,float],
            text:str,
            font_size:float,
            bg_rgb,
            text_rgb:tuple[int,int,int],
            action=None
        ):
        self.mouse_over = False
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]
        self.action = action
        super().__init__()
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]
    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player:
    def __init__(
            self,
            score:int=0,
            health:int=10,
            current_level:int=1,
            diameter:int = 50,
            step_size:int = 100,
            position = (50,50)
        ):
        self.score = score
        self.health = health
        self.current_level = current_level
        self.size = diameter
        self.step_size = step_size

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEW_GAME = 1
    NEXT_LEVEL = 2


def main():
    global screen, clock, grid
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("assets/Outlands.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    game_state = GameState.TITLE
    create_grid()
    while True:
        try:
            if game_state == GameState.TITLE:
                game_state = title_screen(screen)
            if game_state == GameState.NEW_GAME:
                player = Player()
                game_state = play_level(screen, player)
            if game_state == GameState.NEXT_LEVEL:
                player.current_level += 1
                game_state = play_level(screen, player)
            if game_state == GameState.QUIT:
                pygame.quit()
                return
            clock.tick(60)
        except Exception as e:
            print(e)


def title_screen(screen):
    background = pygame.image.load("assets/backgroundgrid.jpg")
    background = pygame.transform.scale(background, (width, height))
    start_btn = UIElement(
        center_position=(width / 2, height / 2 - 30),
        font_size=30,
        bg_rgb=False,
        text_rgb=COLORS["white"],
        text="Start",
        action=GameState.NEW_GAME,
    )
    quit_btn = UIElement(
        center_position=(width / 2, height / 2 + 70),
        font_size=20,
        bg_rgb=False,
        text_rgb=COLORS["white"],
        text="Quit",
        action=GameState.QUIT,
    )
    load_btn = UIElement(
        center_position=(width / 2, height / 2 + 20),
        font_size=25,
        bg_rgb=False,
        text_rgb=COLORS["white"],
        text="Load",
        action=None
    )
    buttons = RenderUpdates(start_btn, quit_btn, load_btn)
    return game_loop(screen, buttons, GameState.TITLE)

def play_level(screen, player):
    return_btn = UIElement(
        center_position=(width / 2, height - 25),
        font_size=20,
        bg_rgb=False,
        text_rgb=COLORS["white"],
        text="Return to menu",
        action=GameState.TITLE,
    )
    nextlevel_btn = UIElement(
        center_position=(width / 2, height / 2),
        font_size=30,
        bg_rgb=False,
        text_rgb=COLORS["white"],
        text=f"Next level ({player.current_level + 1})",
        action=GameState.NEXT_LEVEL,
    )
    buttons = RenderUpdates(return_btn) #nextlevel_btn must be gone for actual release
    return game_loop(screen, buttons, GameState.NEW_GAME)

def create_grid():
    global grid
    grid =[]
    block_number = 1 #number of first block in grid (upper-left)
    for y in range(height// block_size):
        row = []
        for x in range(width//block_size):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            row.append({"rect": rect, "block_number": block_number, "color": COLORS["black"]})
            block_number += 1
        grid.append(row)
    return len(grid)

def draw_grid():
    for row in grid:
        for cell in row:
            pygame.draw.rect(screen, cell["color"], cell["rect"])
            pygame.draw.rect(screen, COLORS["red"], cell["rect"], 1, 20)


def game_loop(screen, buttons, game_state):
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
        if game_state == GameState.TITLE:
            background = pygame.image.load("assets/backgroundgrid.jpg")
            background = pygame.transform.scale(background, (width*2, height))
            screen.blit(background, (0, 0))
        elif game_state == GameState.NEW_GAME:
            screen.fill(COLORS["black"])
            draw_grid()
        else:
            screen.fill(COLORS["black"])
        buttons.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()