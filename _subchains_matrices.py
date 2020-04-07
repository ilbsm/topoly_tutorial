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
# If you are interested in topology of many subchains, consider using
# „matrix" parameter.

topology_map = homfly(structure_open, matrix=True, density=20, level = 10,
                      matrix_plot = True)
print('\n result topology map:', topology_map)


