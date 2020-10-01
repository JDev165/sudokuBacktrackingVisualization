import pygame


class Button:
    def __init__(self, text, width, height, position, text_position):
        self._text = text
        self._width = width
        self._height = height
        self._position = position
        self._color = None
        self._button_rect = pygame.Rect(
            position[0], position[1], width, height)
        self._text_position = text_position

    def get_text_position(self):
        return self._text_position

    def get_text(self):
        return self._text

    def get_rect(self):
        return self._button_rect

    def set_color(self, color):
        self._color = color

    def on_click(self, click_pos):
        clicked = 1 if click_pos[0] < self._position[0] + \
            self._width and click_pos[1] < self._position[1] + self._height else 0

        if clicked:
            print("clicked")
        # clickAction(object)

    def click_action(self, object):
        pass


class SolveButton(Button):
    def __init__(self, text, width, height, position, text_position):
        super().__init__(text, width, height, position, text_position)

    def click_action(self, object):
        object.solve()


class ResetButton(Button):
    def __init__(self, text, width, height, position, text_position):
        super().__init__(text, width, height, position, text_position)

    def click_action(self, object):
        object.reset()


class SkipButton(Button):
    def __init__(self, text, width, height, position, text_position):
        super().__init__(text, width, height, position, text_position)

    def click_action(self, object):
        object.skip()
