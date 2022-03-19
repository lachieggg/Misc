from math import floor
import random
from Algorithms.Algorithm import Algorithm

LENGTH = 2**5
MAX_VALUE = 2**7
CONSOLE_OUTPUT = False

class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__()