class Button:
    def __init__(self, text, width, height, position, text_position):
        self._text = text
        self._width = width
        self._height = height
        self._position = position
        self._color = None
        self._button_rect = Rect(position[0], position[1], width, height)
        self._text_position = text_position

    def setColor(self, color):
        self._color = color

    def onClick(self, clickPos, object):
        clicked = 1 if clickPos[0] < self._width and clickPos[1] < self._height else 0

        if clicked:
            clickAction(object)

    def clickAction(self, object):
        pass


class SolveButton(Button):
    def __init__(self):
        super().__init__()

    def clickAction(self, object):
        object.solve()


class ResetButton(Button):
    def __init__(self):
        super().__init__()

    def clickAction(self, object):
        object.reset()


class SkipButton(Button):
    def __init__(self):
        super().__init__()

    def clickAction(self, object):
        object.skip()
