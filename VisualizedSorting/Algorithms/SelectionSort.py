from math import floor
import random
from Algorithms.Algorithm import Algorithm

LENGTH = 2**5
MAX_VALUE = 2**7
CONSOLE_OUTPUT = False

class SelectionSort(Algorithm):
    """
    A class used to represent an instance of the 
    Selection Sort Algorithm on a particular array

    Selection Sort works by going through each element 
    in the array and swapping it with the smallest element 
    in the rest of the array
    """
    def __init__(self):
        super().__init__()
        self.index = 0
        pass

    def step(self, arr):
        if(self.index == len(arr)):
            self.complete = True
            return arr
        # Swap the smallest element 
        # on the right hand side of the array (i.e. the subarray)
        # with the current element (arr[index])
        subarray = arr[self.index:]
        # Find the smallest element in the subarray
        smallest = subarray.index(min(subarray)) + self.index
       
        arr = self.swap(arr, smallest, self.index)
        self.index += 1
        return arr

