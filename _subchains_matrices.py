from topoly import homfly, plot_matrix, find_spots, translate_matrix
from topoly.params import test

homfly = test(homfly)
plot_matrix = test(plot_matrix)
find_spots = test(find_spots)
translate_matrix = test(translate_matrix)

structure_open='newdata/4ypz.pdb'

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
# If you want check all possible subchains, consider using „matrix" 
# parameter. This parameter lets you calculate invariant over whole 
# spectrum of possible subchains. 

# Consequently, this can take very long time to compute, therefore, 
# function contains the „density" parameter which controls how precisely
# the space of all possible subchains will be explored. For density=1
# all possible subchains are checked. For higher values passed to the 
# density parameter, the number of atoms will be cut and analysed 
# subsequently. 

topology_map = homfly(structure_open, matrix=True, density=100, level = 10,
                      matrix_plot = True)
print('\n result topology map:', topology_map)


