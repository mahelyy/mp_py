import math
import sys

if __name__ == '__main__':

	TOL = float(sys.argv[1])
	outfile = open('eOut.txt', 'w')
	e = math.e
	N = 50
	err = 10

	while err > TOL:
		approx_e = (1 + 1/N)**N
		err = abs(math.e - approx_e) / math.e
		N += 1

	relE = abs(err - e)/e
	outfile.write(f'N = {N}, approx e = {approx_e}, absolute error = {abs(math.e - approx_e)}, relative error = {err}\n')
	outfile.close()
	print(f'N = {N}, approx e = {approx_e}, absolute error = {abs(math.e - approx_e)}, relative error = {err}')


