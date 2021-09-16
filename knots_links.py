from topoly import conway, homfly, yamada
from topoly.params import Closure, PlotFormat, test
from time import perf_counter
"""
In Topoly there are 10 invariant calculating functions. All of them are
used in the same way, so explaining one of them is enough. Let's use
HOMFLYPT polynomial.

Firstly, please read tutorial page: https://tinyurl.com/tkdrrdt
"""
conway = test(conway)
homfly = test(homfly)
yamada = test(yamada)

#=======================
# OPEN AND CLOSED CHAIN
#=======================
print('== Open and closed chain ==')

# We will work with two structures: open and closed one
# First one is artificially created structure of polygon knot 3_1.
structure_closed = 'data/knot31.xyz'
# Second one is TrmD, M1G37 tRNA Methyltransferase. It is open chain,
# as most of proteins is.
structure_open = 'data/4ypz.pdb'

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
# a tradeoff for possibility of finding knot type of open chain.


#=================
# NUMBER OF TRIES
#=================
print('\n\n== Number of tries ==')

# If you want to have you calculation more accurate (or give up 
# accuracy for faster calculation), use „tries" parameter. It describes
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
                                                                                
subchain = homfly(structure_open, chain_boundary=[[3,40]])                                 
subchains = homfly(structure_open, chain_boundary=[[3,40],[40,80]])                        
                                                                                
print('\n result subchain:', subchain)                                          
print('\n result subchains:', subchains) 

#==========
# KNOT MAP
#==========
print('\n\n== Knot map ==')
# If you want check all possible subchains, consider using „matrix"
# parameter. This parameter lets you calculate invariant over whole
# spectrum of possible subchains.

# Consequently, this can take very long time to compute, therefore,
# function contains the „density" parameter which controls how precisely
# the space of all possible subchains will be explored. For density=1
# all possible subchains are checked. For higher values passed to the
# density parameter, the number of atoms will be cut and analysed
# subsequently.

# Here we use conway polynomial (it is faster then homfly), with
# parameter „tries=10", to make possible calculating whole matrix
# on ordinary computer quickly.

polygon='data/knot51.xyz'
knot_matrix = conway(polygon, tries=10, matrix=True, matrix_density=1, 
                matrix_calc_cutoff=0, matrix_map=True, 
                map_fileformat = PlotFormat.PDF, map_filename = 'map_knot')
print('\n resulting knot matrix:\n', knot_matrix)

# For more info about matrix manipulation check „matrices.py".
