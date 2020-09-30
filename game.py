import pygame
from pygame.locals import *


class Console:
    def __init__(self, cartridge, font, screenSize):
        self._cartridge = cartridge
        self._font = font
        self._screenSize = screenSize
        self._screen = None
        self._running = True

    def playGameCartridge(self):
        pygame.init()
        font = pygame.font.SysFont(self.gameFont, 35)
        self.screen = pygame.display.set_mode(self.screenSize)

        self.cartridge.play(pygame)

    def _game_loop(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:

                elif event.type == pygame.KEYDOWN:

            pygame.display.set_caption("Sudoku")
            screen.fill(WHITE)
            pygame.draw.rect(screen, BLACK, sudoku_board, 1)

            pygame.display.update()

        pygame.quit()
