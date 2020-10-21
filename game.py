import pygame
from constants import *
from pygame.locals import *
from sudoku_cartridge import *


class Console:
    def __init__(self, cartridge, font_name, screenSize):
        self._cartridge = cartridge
        self._font_name = font_name
        self._screenSize = screenSize
        self._screen = None
        self._running = True
        pygame.init()
        self._font = pygame.font.SysFont(self._font_name, 35)
        self._cartridge.setFont(self._font)
        self._screen = pygame.display.set_mode(self._screenSize)

    def play_cartridge(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._cartridge.mouseClickEvent(pygame.mouse.get_pos())
                elif event.type == pygame.KEYDOWN:
                    pass

            pygame.display.set_caption("Sudoku")
            self._screen.fill(WHITE)
            sudoku_board = self._cartridge.getBoard()
            pygame.draw.rect(self._screen, BLACK, sudoku_board, 1)

            self._screen = self._cartridge.play(self._screen)

            pygame.display.update()

        pygame.quit()


def main():
    sudoku_cartridge = Sudoku('Sudoku', SUDOKU_BOARD_SIZE)
    console = Console(sudoku_cartridge, 'arial', SCREEN_SIZE)
    console.play_cartridge()


if __name__ == "__main__":
    main()
