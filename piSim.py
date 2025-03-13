import sys
import random
import math

if __name__ == '__main__':
	N_values = [10, 100, 1000, 1000000]
	for N in N_values:
		inside_circle = 0
		for _ in range(N):
			x = random.random()
			y = random.random()
			if sqrt(x*x + y*y) < 1:
				inside_circle += 1
	pi_approx = 4 * inside_circle /N
	absolute_error = abs(math.pi - pi_approx)
	relative_error = absolute_error / math.pi
	print(f'N ={N}, approx pi = {pi_approx}, absolute error = {absolute_error}, relative error = {relative_error}')

