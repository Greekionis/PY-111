"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
import numpy as np
import random
def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	print(arr)
	return -1

def find(find_elem, array):

	index = None
	for i, elem in enumerate(array):
		if elem == find_elem:
			index = i
			return index
	return index



if __name__ == "__main__":
	r = 1000
	array = np.random.randint(0, r, r)
	find_elem = np.random.choice(array)
	print(find_elem)
	print(find(find_elem, array))