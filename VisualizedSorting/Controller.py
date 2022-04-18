#!/usr/bin/env python3

import sys

from Window import Window

from Constants import * 

from Algorithms.MergeSort import MergeSort
from Algorithms.QuickSort import QuickSort
from Algorithms.BubbleSort import BubbleSort
from Algorithms.InsertionSort import InsertionSort
from Algorithms.SelectionSort import SelectionSort


class Controller:
    def __init__(self):
        # Window
        self.initAlgorithm()
        self.arr = self.algorithm.initArray()
        self.window = Window(self.algorithm)

    def main(self):
        self.window.main()
    
    def initAlgorithm(self):
        try: 
            self.algorithm = eval(ALGORITHM)
        except NameError:
            print(ALGORITHM_NOT_FOUND)
            exit()

if(__name__ == "__main__"):
    print("Click to begin the algorithm.")
    try:
        c = Controller()
        c.main()
    except KeyboardInterrupt:
        print('\nExiting.')
