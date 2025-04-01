import sys
import time

from scripts.ui import *
from scripts.grid import *
from scripts.classes import *
from scripts.mydict import *

# Initialize Pygame
py.init()
py.mixer.init()

# Load Music
music = py.mixer.music
music.load("assets/sounds/music.mp3")
music.set_volume(0.5)

# Screen Settings
width, height = 1000, 1000
screen = py.display.set_mode((width, height))
clock = py.time.Clock()

# Grid Setup
grid_1 = Grid(surface=screen, width=width, height=height, cell_size=100,
              corner_radius=10, body_rgb=black,
              line_rgb=red)

# Game State
running = True
game_started = False

# Create Player
player = Player(25, color=red, pos=Vector2(50, 50),grid=grid_1)
all_sprites = py.sprite.Group(player)


def start_game():
    """In-game loop"""
    global game_started, running
    game_started = True  # Switch to game screen
    while game_started and running:
        try:
            screen.fill(black)  # Clear the screen
            grid_1.draw()
            mouse_pos = py.mouse.get_pos()
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                    game_started = False
                elif event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                    game_started = False  # Return to menu

            # Only allow player movement if it's their turn
            if player.turn:
                player.handle_input(screen_width=width, screen_height=height)
                print(player.current_cell)

            elif not player.turn:
                py.time.delay(300)  # Simulate enemy/AI turn
                player.turn = True  # Give control back to player

            # Update and draw sprites
            all_sprites.update(screen)

            # Refresh the screen
            py.display.flip()
            clock.tick(60)  # Limit FPS
        except Exception as e:
            print("Error in game loop:", e)
            time.sleep(10)
            break


def load_game():
    """Load game state and start game loop"""
    print("Load game (Placeholder)")  # Placeholder function


def exit_game():
    """Save game state and exit"""
    py.quit()
    sys.exit()


# Menu Buttons
menu_buttons = [
    UIElement(center_position=(width // 2, 400), text="Start", font_size=30, bg_rgb=False, text_rgb=white,
              text_highlight_rgb=red,action=start_game),
    UIElement(center_position=(width // 2, 500), text="Load", font_size=30, bg_rgb=False, text_rgb=white,
              text_highlight_rgb=red,action=load_game),
    UIElement(center_position=(width // 2, 600), text="Exit", font_size=30, bg_rgb=False, text_rgb=white,
              text_highlight_rgb=red,action=exit_game)
]


def main():
    """Main menu loop"""
    global game_started, running
    py.mixer.music.play(-1)  # Play background music

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
                    if game_started:
                        game_started = False  # Return to menu

            if not game_started:
                for button in menu_buttons:
                    action = button.update(mouse_pos, mouse_up)
                    if action: action()
                    button.draw(screen)

            py.display.flip()
            clock.tick(60)
        except Exception as e:
            print("Error in main loop:", e)


if __name__ == "__main__":
    main()
