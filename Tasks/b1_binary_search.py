from typing import Any, Sequence, Optional
import numpy as np

# def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
# 	"""
# 	Performs binary search of given element inside of array
#
# 	:param elem: element to be found
# 	:param arr: array where element is to be found
# 	:return: Index of element if it's presented in the arr, None otherwise
# 	"""
# 	print(elem, arr)
# 	return None

def binary_search(find_elem, array):
	start = 0
	end = len(array)

	if find_elem >= 0:
		while True:
			middle = int(end/2)
			end = len(array)
			print(array[middle])
			if array[middle] == find_elem:
				return array[int(middle+1)]
			elif find_elem > array[middle]:
				if middle != 0:
					array = array[middle:end]
				else:
					return array[int(middle+1)]
			elif find_elem < array[middle]:
				if middle != 0:
					array = array[start:middle]

			end = int(end/2)

	else:
		return None
	#return end





if __name__ == "__main__":
	r = 100
	array = np.array([i for i in range(r)])
	#find_elem = np.random.choice(array)
	#find_elem = 747  # !
	find_elem = 100
	print(array)
	print("Ищем {}".format(find_elem))
	print(binary_search(find_elem, array))