from math import floor
import random

from Algorithms.Algorithm import Algorithm
from Constants import *

class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__()


    def step(self, arr):
        end = False
        for j in range(len(arr)):
            for i in range(1, len(arr)):
                if(arr[i-1] > arr[i]):
                    arr = self.swap(arr, i, i-1)
                    end = True
                    break
            if(end):
                break
        return arr

    def bubbleSort(self, arr, window):
        for j in range(len(arr)):
            if(VISUALIZE): visualize(arr)
            for i in range(1, len(arr)):
                if(arr[i-1] > arr[i]):
                    arr = self.swap(arr, i, i-1)		
        return arr

