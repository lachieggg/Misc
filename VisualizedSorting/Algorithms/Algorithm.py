
import os
import sys
import random

from Constants import *

class Algorithm:
    def __init__(self):
        self.add_to_sys_path()
        self.complete = False
        pass

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        return arr

    def initArray(self):
        arr = [x for x in range(LENGTH)]
        for i in range(LENGTH):
            arr[i] = random.randint(0, MAX_VALUE)
                    
        self.arr = arr
        return arr

    def add_to_sys_path(self):
        """Add root folder to the path allowing imports from subdirectories"""
        sys.path.append(os.path.abspath('../'))

    def main(self):
        """Main function which creates the controller object"""
        # Sys
        add_to_sys_path()