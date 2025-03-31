import dict, grid, pygame as py, ui, sys

py.init()
py.mixer.init()

music = py.mixer.music
music.load("assets/sounds/Outlands.mp3")
music.set_volume(0.5)

width, height = 1000, 1000
screen = py.display.set_mode((width, height))
grid_1 = grid.Grid(width=width,height=height,rect_size=100,
                     corner_radius=10,body_rgb=dict.black,
                     line_rgb=dict.red)
grid_1.set_surface(screen)
ui_element = ui.UIElement

clock = py.time.Clock()

running = True
game_started = False

def start_game():
    global game_started
    game_started = True  # Switch to game screen
    return game_started


def load_game():
    print("Load game (Placeholder)")  # Placeholder for loading game


def exit_game():
    """save game state and exit"""
    py.quit()
    sys.exit()


buttons = [
    ui_element(center_position=(width // 2, 250), text="Start", font_size=30, bg_rgb=False, text_rgb=dict.white, action=start_game),
    ui_element(center_position=(width // 2, 350), text="Load", font_size=30, bg_rgb=False, text_rgb=dict.white, action=load_game),
    ui_element(center_position=(width // 2, 450), text="Exit", font_size=30, bg_rgb=False, text_rgb=dict.white, action=exit_game),
]


def main():
    global game_started, running
    py.mixer.music.play(-1)
    while running:
        try:
            screen.fill(dict.black)
            mouse_pos = py.mouse.get_pos()
            mouse_up = False
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                elif event.type == py.MOUSEBUTTONUP:
                    mouse_up = True
                    if game_started:
                        grid_1.handle_events(event, primary_color=dict.green, secondary_color=dict.black)
                elif event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                    if game_started: game_started = False  # Return to menu
            if game_started:
                # In-Game Screen
                grid_1.draw()
            if not game_started:
                for button in buttons:
                    action = button.update(mouse_pos, mouse_up)
                    if action: action()
                    button.draw(screen)
            py.display.flip()
            clock.tick(60)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()