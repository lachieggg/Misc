from math import floor
import random
from Algorithms.Algorithm import Algorithm


class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__()        
        self.sorted = []
        self.original = self.initArray()
        self.counter = 0
        pass

    def insert(self, A, elem, index):
        B = A[0:index]
        B.append(elem)
        for x in A[index:]:
            B.append(x)
        return B

    def step(self, L):
        """One step of insertion sort"""
        end = False

        if(self.counter == len(self.original)):
            self.complete = True
            return self.sorted

        x = self.original[self.counter]

        # Start position
        index = 0
        if(len(self.sorted) == 0):
            self.sorted.append(self.original[0])
            self.counter += 1
            return self.sorted

        if(x < self.sorted[0]):
            self.sorted.insert(0, x)
            self.counter += 1
            return self.sorted

        # End position
        index = len(self.sorted)
        if(x > self.sorted[index-1] and index > 0):
            self.sorted.insert(index, x)
        
        # Middle position(s)
        j = 0
        while(j <= len(self.sorted)):
            prev = self.sorted[j-1]
            curr = self.sorted[j]

            if(x >= prev and x <= curr):
                self.sorted.insert(j, x)
                break
            j += 1

        self.counter += 1
        return self.sorted
