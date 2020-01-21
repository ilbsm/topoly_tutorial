#!/usr/bin/python3
from time import time

from topoly import import_coords, yamada, homfly, alexander, conway, \
    jones, yamada, blmho, kauffman_bracket, kauffman_polynomial, Closure, TopolyException
#yamada, homfly, alexander, conway,
algos = [yamada, alexander, conway, jones, blmho, kauffman_bracket, kauffman_polynomial]

file = 'data/1j85.pdb'
file = 'data/31.xyz'
with open(file, 'r') as myfile:
    data = myfile.read()
curve = import_coords(data)
for algo in algos:
    try:
        t0 = time()
        print(algo.__name__, ' : ', algo(curve, matrix=True, closure=Closure.TWO_POINTS, tries=10, matrix_plot=True,
                                         output_file=algo.__name__+'.txt', plot_ofile=algo.__name__, translate=True,
                                         run_parallel=True, parallel_workers=None))
        t = time()-t0
        print('Done {0} in {1} s.'.format(algo.__name__, round(t, 3)))
    except TopolyException as ve:
        print(algo.__name__, ' : ' + str(ve))
