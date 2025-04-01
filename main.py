import sys, pygame as py
from scripts.ui import *
from scripts.grid import *
from scripts.classes import *
from scripts.mydict import *

py.init()
py.mixer.init()

music = py.mixer.music
music.load("assets/sounds/music.mp3")
music.set_volume(0.5)

width, height = 1000, 1000
screen = py.display.set_mode((width, height))
grid_1 = Grid(width=width, height=height, rect_size=100,
              corner_radius=10, body_rgb=black,
              line_rgb=red)
grid_1.set_surface(screen)

clock = py.time.Clock()

running = True
game_started = False

all_sprites = py.sprite.Group() # declare sprite group
player = Player(width=25, height= 25,color=white, pos=vec(50,50)) # call player class with params
all_sprites.add(player) # add player to sprite group ( for collision and general interaction w/ other sprites )


def start_game():
    """in-game loop"""
    global game_started, running
    game_started = True  # Switch to game screen
    while game_started and running:
        try:
            screen.fill(black)
            grid_1.draw()
            mouse_pos = py.mouse.get_pos()
            mouse_up = False
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                    game_started = False  # Make sure to exit loop
                elif event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                    game_started = False  # Return to main menu
                elif event.type == py.MOUSEBUTTONUP:
                    mouse_up = True
                    grid_1.handle_events(event, primary_color=white, secondary_color=black)
            for entity in all_sprites:
                entity.update(screen)
            py.display.flip()  # Update the display
            clock.tick(60)  # Limit FPS to prevent freezing
        except Exception as e:
            print(e)


def load_game():
    """load game state and start game loop"""
    print("Load game (Placeholder)")  # Placeholder for loading game


def exit_game():
    """save game state and exit"""
    py.quit()
    sys.exit()


menu_buttons = [
    UIElement(center_position=(width // 2, 250), text="Start", font_size=30, bg_rgb=False, text_rgb=white,
              action=start_game),
    UIElement(center_position=(width // 2, 350), text="Load", font_size=30, bg_rgb=False, text_rgb=white,
              action=load_game),
    UIElement(center_position=(width // 2, 450), text="Exit", font_size=30, bg_rgb=False, text_rgb=white,
              action=exit_game),
]


def main():
    """main loop handling events outside of game loop"""
    global game_started, running
    py.mixer.music.play(-1)
    while running:
        try:
            screen.fill(black)
            mouse_pos = py.mouse.get_pos()
            mouse_up = False
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                elif event.type == py.MOUSEBUTTONUP:
                    mouse_up = True
                elif event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                    if game_started: game_started = False  # Return to menu
            if not game_started:
                for button in menu_buttons:
                    action = button.update(mouse_pos, mouse_up)
                    if action: action()
                    button.draw(screen)
            py.display.flip()
            clock.tick(60)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
