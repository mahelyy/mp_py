import math
import sys

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: approxE.py <TOL>")
		sys.exit(1)

	TOL = float(sys.argv[1])
	outfile = open('eOut.txt', 'w')
	N = 1
	err = 1.0

	while err > TOL:
		approx_e = (1 + 1/N)**N
		err = abs(math.e - approx_e) / math.e
		N = N*10

	outfile.write(f'N = {N}, approx e = {approx_e}, absolute error = {abs(math.e - approx_e)}, relative error = {err}\n')
	outfile.close()
	print(f'N = {N}, approx e = {approx_e}, absolute error = {abs(math.e - approx_e)}, relative error = {err}')


