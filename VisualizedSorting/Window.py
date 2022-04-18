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
        self.screen.fill(BACKGROUND)
        self.algorithm = algorithm
        self.arr = self.algorithm.initArray()
        self.colours = {}
        if(CONSTANT):
            for elem in self.arr:
                self.colours[elem] = self.randomColour()

    def resetDisplay(self):
        self.screen.fill(BACKGROUND)
    
    def draw(self, x, y, height):
        if(RANDOM):
            colours = (height%randint(1,255), height%randint(1,255), height%randint(1,255))
        elif(GRAY):
            colours = (height, height, height)
        elif(CONSTANT):
            colours = self.colours[height]

        pygame.draw.rect(self.screen,
		colours,
		[x, y, RECT_WIDTH, height]
	)

    def randomColour(self):
        return (randint(1,255), randint(1,255), randint(1,255))

    def visualize(self, arr):
        self.resetDisplay()
        for index, element in enumerate(arr):
            px = SPACING_SIZE*index+SIDELINE
            self.draw(px, SCREEN_HEIGHT-element-BASELINE, element)

    def run(self):
        pygame.time.wait(TIME_SLEEP)
        self.arr = self.algorithm.step(self.arr)
        self.visualize(self.arr)

    def main(self):
        """Main PyGame loop"""
        running = True
        visualized = False
        started = False

        while running:
            if(visualized and started and not self.algorithm.complete):
                self.run()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False

                if event.type == MOUSEBUTTONDOWN:
                    if(not visualized):
                        self.visualize(self.arr)
                        visualized = True
                    else:
                        started = True

            pygame.display.flip()

        pygame.quit()
