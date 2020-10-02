import pygame


class Button:
    def __init__(self, text, width, height, position, text_position, object):
        self._text = text
        self._width = width
        self._height = height
        self._position = position
        self._color = None
        self._button_rect = pygame.Rect(
            position[0], position[1], width, height)
        self._text_position = text_position
        self._object = object

    def get_text_position(self):
        return self._text_position

    def get_text(self):
        return self._text

    def get_rect(self):
        return self._button_rect

    def set_color(self, color):
        self._color = color

    def on_click(self, click_pos):
        if self.clicked(click_pos):
            self.click_action()

    def clicked(self, click_pos):
        return 1 if ((self._position[0] <= click_pos[0]) and (self._position[0] + self._width >= click_pos[0]) and (self._position[1] <= click_pos[1]) and (self._position[1] + self._height >= click_pos[1])) else 0

    def click_action(self):
        pass


class SolveButton(Button):
    def __init__(self, text, width, height, position, text_position, object):
        super().__init__(text, width, height, position, text_position, object)

    def click_action(self):
        self._object.solve()


class ResetButton(Button):
    def __init__(self, text, width, height, position, text_position, object):
        super().__init__(text, width, height, position, text_position, object)

    def click_action(self):
        self._object.reset()


class SkipButton(Button):
    def __init__(self, text, width, height, position, text_position, object):
        super().__init__(text, width, height, position, text_position, object)

    def click_action(self, object):
        self._object.skip()
