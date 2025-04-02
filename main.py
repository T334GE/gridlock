import sys, time
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
title_img = py.image.load("assets/img/title.png")
clock = py.time.Clock()

# Grid Setup
grid_1 = Grid(surface=screen, width=width, height=height, cell_size=50,
              corner_radius=8, body_rgb=black,
              line_rgb=green)

# Game State
running = True
game_started = False
paused = False

# Create Player
player = Player(15, color=white, pos=Vector2(25, 25),grid=grid_1,step_size=grid_1.cell_size)
all_sprites = py.sprite.Group(player)


def start_game():
    """In-game loop"""
    global game_started, running, paused
    game_started = True  # Switch to game screen
    paused = False
    last_cell = None  # Track the last cell player stood on

    while game_started and running:
        try:
            # Handle events in game
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                    game_started = False
                elif event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                    pause_game()  # Toggle pause state
            screen.fill(black)
            grid_1.draw()
            if not paused:
                mouse_pos = py.mouse.get_pos()
                player_cell = grid_1.get_this_cell(player.pos)
                target_cell = grid_1.get_this_cell(mouse_pos)
                if last_cell and last_cell != player_cell: # reset color of cell if player left it
                    last_cell["color"] = grid_1.body_rgb  # original color
                    grid_1.draw_cell(last_cell)
                    py.display.update(last_cell["rect"])
                if player_cell:
                    player_cell["color"] = green  # Highlight color
                    grid_1.draw_cell(player_cell)# Highlight the cell
                    last_cell = player_cell  # Update the last cell
                if player.turn:
                    player.handle_input()
                elif not player.turn:
                    py.time.delay(500)  # Simulate enemy/AI turn
                    player.turn = True  # Give control back to player

                all_sprites.update(screen) # Update and draw sprites
            else: # Draw pause screen
                pause_text = py.font.SysFont('JetBrains Mono Regular', 72).render("PAUSED", True, white)
                screen.blit(pause_text, (width // 2 - pause_text.get_width() // 2,
                                         height // 2 - pause_text.get_height() // 2))

                # Draw pause menu buttons
                for button in pause_menu_buttons:
                    mouse_pos = py.mouse.get_pos()
                    mouse_up = False
                    for event in py.event.get():
                        if event.type == py.MOUSEBUTTONUP:
                            mouse_up = True

                    action = button.update(mouse_pos, mouse_up)
                    if action:
                        action()
                    button.draw(screen)
            py.display.flip() # Refresh screen
            clock.tick(60)  # Limit FPS
        except Exception as e:
            print("Error in game loop:", e)
            time.sleep(1)

def load_game():
    """Load game state and start game loop"""
    print("Load game (Placeholder)")  # Placeholder function

def pause_game():
    global paused
    paused = not paused  # Toggle pause state


def exit_game():
    """Save game state and exit"""
    py.quit()
    sys.exit()


menu_buttons = [
    Text_Button(center_position=(width // 2, height // 2 - 100), text="Start", font_size=40, bg_rgb=False, text_rgb=white,
                text_highlight_rgb=green, action=start_game),
    Text_Button(center_position=(width // 2, height // 2), text="Load", font_size=30, bg_rgb=False, text_rgb=white,
                text_highlight_rgb=green, action=load_game),
    Text_Button(center_position=(width // 2, height // 2 + 100), text="Exit", font_size=25, bg_rgb=False, text_rgb=white,
                text_highlight_rgb=green, action=exit_game)
]

pause_menu_buttons = [
    Text_Button(center_position=(width // 2, height // 2 + 100), text="Resume", font_size=30, bg_rgb=False, text_rgb=white,
                text_highlight_rgb=green, action=pause_game)
]

def main():
    """Main menu loop"""
    global game_started, running, paused
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
                    if not game_started:
                        exit_game()

            if not game_started: # title screen
                screen.blit(title_img,(0,0))
                for button in menu_buttons:
                    action = button.update(mouse_pos, mouse_up)
                    if action:
                        action()
                    button.draw(screen)

            py.display.flip()
            clock.tick(60)
        except Exception as e:
            print("Error in main loop:", e)
            time.sleep(1)


if __name__ == "__main__":
    main()
