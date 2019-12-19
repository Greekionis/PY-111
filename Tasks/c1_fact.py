def factorial_recursive(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in recursive way
	:param n: int > 0
	:return: factorial of n
	"""
	if n < 0:
		raise ValueError
	elif n == 1:
		return 1
	else:
		return factorial_recursive(n - 1) * n


	print(n)
	return 0


def factorial_iterative(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in iterative way

	:param n: int > 0
	:return: factorial of n
	"""

	if n < 0:
		raise ValueError
	else:
		if n == 0:
			return 1
		else:
			p = 1
			for i in range(1, n+1):
				p *= i
			return p

	print(n)
	#return 0

print(factorial_iterative(5))