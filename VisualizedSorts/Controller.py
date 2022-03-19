#!/usr/bin/env python3

import sys
import os

from Window import Window

from threading import Thread
from time import sleep

from Algorithms.MergeSort import MergeSort
from Algorithms.QuickSort import QuickSort
from Algorithms.BubbleSort import BubbleSort
from Algorithms.InsertionSort import InsertionSort
from Algorithms.SelectionSort import SelectionSort

ALGORITHM = InsertionSort

class Controller:
    def __init__(self):
        # Window
        self.algorithm = ALGORITHM()
        self.arr = self.algorithm.initArray()
        self.window = Window(self.algorithm)

    def main(self):
        self.window.main()

if(__name__ == "__main__"):
    c = Controller()
    c.main()
