"""
Taylor series
"""
from typing import Union
import math


def ex(x: Union[int, float]) -> float:
	"""
	Calculate value of e^x with Taylor series

	:param x: x value
	:return: e^x value
	"""

	if x == 0:
		return 1
	else:
		result_sum = 1
		n = 1
		delta = 0.00001
		while True:
			result = (x**n) / math.factorial(n)
			if result < delta:
				return result_sum
			else:
				result_sum += result
				n += 1

	print(x)
	return 0


def sinx(x: Union[int, float]) -> float:
	"""
	Calculate sin(x) with Taylor series

	:param x: x value
	:return: sin(x) value
	"""

	
	print(x)
	return 0

