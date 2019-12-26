import numpy as np


def calculate_paths(shape: (int, int), point: (int, int)) -> int:
	"""
	Given field with size rows*cols count available paths from (0, 0) to point

	:param shape: tuple of rows and cols (each from 1 to rows/cols)
	:param point: desired point for horse
	:return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
	"""

	F = np.zeros(shape, dtype=np.int32)
	#print(F)
	N = shape[0]
	M = shape[1]
	#print(shape[1])

	F[0, 0] = 1
	for i in range(shape[0]):  # Проход по строкам
		for j in range(shape[1]):  # Проход по столбцам
			if F[i, j] != 0:
				if (i + 1 < N) and (j + 2 < M):
					F[i + 1, j + 2] += F[i, j] * 2
				if (i + 1 < N) and (j - 2 >= 0):
					F[i + 1, j - 2] += F[i, j] * 2
				# На 2 клетки вниз и одну вправо
				if (i + 2 < N) and (j + 1 < M):
					F[i + 2, j + 1] += F[i, j] * 2
				if (i + 2 < N) and (j - 1 >= 0):
					F[i + 2, j - 1] += F[i, j] * 2


	#print(shape, point)
	print(F)
	return F[point]

if __name__ == "__main__":
	n = 8
	m = 8
	point = (7, 7)
	print(calculate_paths((n, m), point))