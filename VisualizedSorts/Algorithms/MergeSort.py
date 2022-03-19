from math import floor
import random

LENGTH = 50
MAX_VALUE = 2**7
CONSOLE_OUTPUT = False

import pygame
from Algorithms.Algorithm import Algorithm

class MergeSort(Algorithm):
	def __init__(self):
		super().__init__()
		self.index = 0

	def merge(self, A, B):
		if(len(A) == 0):
			return B
		if(len(B) == 0):
			return A

		self.index += 1
		if(A[0] <= B[0]):
			arr = [A[0]] + self.merge(A[1:], B)
		else:
			arr = [B[0]] + self.merge(A, B[1:])

		return arr

	def mergeSort(self, arr):
		if(CONSOLE_OUTPUT): print("Input array {}".format(arr))
		if(len(arr) > 1):
			n = len(arr)
			A = arr[0:floor(n/2)]
			B = arr[floor(n/2):n]
			return self.merge(self.mergeSort(A), self.mergeSort(B))
		else:
			return arr
	
	def main(self, arr):
		self.arr = arr
		sorted = self.mergeSort(arr)