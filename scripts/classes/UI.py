import pygame as py, pygame_gui as pygui

class UI:
    def __init__(self, manager:pygui.ui_manager.UIManager):
        self.manager = manager

        self.menu_container = pygui.elements.UIPanel(
            py.Rect(-1, -1, 200, 300),
            anchors={"center": "center"},
            object_id="main_menu_container"
        )

        self.start_button = pygui.elements.UIButton(
            py.Rect(-1, 50, 75, -1),
            text="start",
            anchors={"centerx": "centerx",
                     "bottom_target": "exit_button"},
            container=self.menu_container,
            object_id="start_btn"
        )

        self.exit_button = pygui.elements.UIButton(
            py.Rect(-1, 100, 75, -1),
            text="exit",
            anchors={"centerx": "centerx",
                     "top_target": "start_button"},
            container=self.menu_container,
            object_id="exit_btn"
        )