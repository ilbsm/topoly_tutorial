from topoly import (alexander, jones, conway, homfly, kauffman_bracket, 
                    kauffman_polynomial, blmho, yamada, aps, writhe)
from topoly.params import Closure, test
from time import perf_counter
"""
In Topoly there are 10 invariant calculating functions. All of them are
used in the same way, so explaining one of them is enough. Let's use
HOMFLYPT polynomial.

Firstly, please read tutorial page: https://tinyurl.com/tkdrrdt
"""
homfly = test(homfly)

#=======================
# OPEN AND CLOSED CHAIN
#=======================
print('== Open and closed chain ==')

# We will work with two structures: open and closed one
# First one is artificially created structure of polygon knot 3_1.
structure_closed = 'newdata/knot31.xyz'
# Second one is TrmD, M1G37 tRNA Methyltransferase. It is open chain,
# as most of proteins is.
structure_open = 'newdata/4ypz.pdb'

# Let's start with closed chain polygon. Simplest usage looks like that:
closed_chain = homfly(structure_closed, closure=Closure.CLOSED)
print('\nresult closed chain:', closed_chain)
# closure=Closure.CLOSED means that first and last point of chain will
# be treated as connected

# If you have open chain, then it is necessary to close chain. Simplest
# usage looks like that:
open_chain = homfly(structure_open)
print('\nresult open chain:',open_chain)


#================
# OTHER CLOSURES
#================
print('\n\n== Other closures ==')

# You can use other methods of closing, default is Closure.TWO_POINTS.
# Other are:
mass_center = homfly(structure_open, closure=Closure.MASS_CENTER)
direction = homfly(structure_open, closure=Closure.DIRECTION)
one = homfly(structure_open, closure=Closure.ONE_POINT)
rays = homfly(structure_open, closure=Closure.RAYS)
print('\nresult MASS_CENTER:',  mass_center)
print('\nresult DIRECTION:', direction)
print('\nresult ONE_POINT:', one)
print('\nresult RAYS:', rays)

# As you see, the result depends on chosen closure method. It is
# a tradeoff for posibility of finding knot type of open chain.


#=================
# NUMBER OF TRIES
#=================
print('\n\n== Number of tries ==')

# If you want to have you calculation more accurate (or give up 
# accuracy for faster calcukation), use „tries" parameter. It describes
# how many times calculation will be repeated. This parameter only makes
# sense for probabilistic closure methods: TWO_POINTS (default), 
# ONE_POINT and RAYS. Lets run function with three different values of
# tries (20, 200, 2000):

start = perf_counter()
fast = homfly(structure_open, tries = 20)
stop = perf_counter()
print('\nresult tries=20: ', fast)
print('calculation time: {:f} s'.format(stop-start))

start = perf_counter()
default = homfly(structure_open, tries = 200)
stop = perf_counter()
print('\nresult tries=200: ', default)
print('calculation time: {:f} s'.format(stop-start))

start = perf_counter()
accurate = homfly(structure_open, tries = 2000)
stop = perf_counter()
print('\nresult tries=2000: ', accurate)
print('calculation time: {:f} s'.format(stop-start))


#===========
# CHIRALITY
#===========
print('\n\n== Chirality ==')

# If you are interested in chirality of your structures, then use 
# „chirality = True" argument. Remember that not every invariant can
# distinguish chiral structures!

achiral = homfly(structure_open)
chiral  = homfly(structure_open, chiral = True)
print('\n result achiral:', achiral)
print('\n result chiral:', chiral)


#===========
# SUBCHAINS
#===========
print('\n\n== Subchains ==')
# Using parameter „boundaries" you can find topology of fragment of 
# passed chain.

subchain = homfly(structure_open, boundaries=[[3,40]])
subchains = homfly(structure_open, boundaries=[[3,40],[40,80]])

print('\n result subchain:', subchain)
print('\n result subchains:', subchains)


#==============
# TOPOLOGY MAP
#==============
print('\n\n== Topology map ==')
# If you are interested in topology of many subchains, consider using  
# „matrix parameter".

topology_map = homfly(structure_open, matrix=True, density=100, level = 0.1, 
                      matrix_plot = True)
print('\n result topology map:', topology_map)





