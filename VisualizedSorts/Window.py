import sys
import pygame
import os

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)

from Constants import *

from random import randint


class Window:
    def __init__(self, algorithm):
        """Initializer for the Window"""
        pygame.init()
        pygame.display.set_caption('SortVisualizer')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((255, 255, 255))
        self.algorithm = algorithm
        self.arr = self.algorithm.initArray()
        self.rands = [randint(0,255), randint(0,255), randint(0,255)]

    def resetDisplay(self):
        self.screen.fill((255, 255, 255))

    def draw(self, x, y, height):
        colours = (height%self.rands[0], height%self.rands[1], height%self.rands[2])
        pygame.draw.rect(self.screen,
		colours,
		[x, y, RECT_WIDTH, height]
	)

    def visualize(self, arr):
        self.resetDisplay()
        for index, element in enumerate(arr):
            px = SPACING_SIZE*index+SIDELINE
            self.draw(px, SCREEN_HEIGHT-element-BASELINE, element)

    def algo(self):
        pygame.time.wait(TIME_SLEEP)
        self.arr = self.algorithm.step(self.arr)
        self.visualize(self.arr)

    def main(self):
        """Main PyGame loop"""
        running = True

        while running:
            if(not self.algorithm.complete):
                self.algo()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False

                if event.type == MOUSEBUTTONDOWN:
                    pass

            pygame.display.flip()

        pygame.quit()
