from topoly import conway, gln, plot_matrix, find_spots, translate_matrix
from topoly.params import Closure, PlotFormat, OutputFormat, test

"""
If you want to check all possible subchains for knotting or to calculate
GLN values then you should check matrices. Be aware, that calculating
with maximal precision is computationaly hard job and probably you need
supercomputer. In this tutorial examples are chosen in such a way,
that calculation should be possible on ordinary computer.
"""

plot_matrix = test(plot_matrix)
find_spots = test(find_spots)
translate_matrix = test(translate_matrix)

polygon = 'data/knot51.xyz'
arc1    = 'data/arc1.xyz'                                                       
arc2    = 'data/arc2.xyz' 
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

knot_matrix = conway(polygon, tries=10, matrix=True, matrix_density=1, 
                matrix_calc_cutoff=0, matrix_map=True, 
                matrix_format = PlotFormat.PDF, map_filename = 'map_knot')
print('\n resulting knot matrix:', knot_matrix)

#===================================
# GAUSSIAN LINKING NUMBER (GLN) MAP
#===================================
print('\n\n== GLN map ==')
# If you are more interested in GLN subchain values you can use matrix 
# mode. In this mode you will get GLN values between first arc and all 
# possible subchains of arc2:
                                                                                
gln_matrix = gln(arc2, arc1, matrix=True, matrix_map=True, 
                 map_filename='map_gln', map_fileformat=PlotFormat.PDF)
print('\n resulting gln matrix:', gln_matrix)

#=====================
# MATRIX MANIPULATION
#=====================
print('\n\n== Matrix manipulation ==')

# Defaultly gln_matrix is represented as list of list, and knot_matrix
# defaultly is represented as a dictionary. This can be changed using:
# * output_format parameter (output_format=OutputFormat.Dictionary,
#                            output_format=OutputFormat.Matrix) 
# * or translate_matrix function which changes representation of given
# matrix.

translate_matrix(knot_matrix, output_format=OutputFormat.Matrix)
translate_matrix(gln_matrix, output_format= OutputFormat.Dictionary)

# find_spots finds geometrical centers of each identified topology
# field.

#knot_centers = find_spots(knot_matrix, gap_size = 0, spot_size = 5)
gln_centers = find_spots(gln_matrix, gap_size = 0, spot_size = 5)
#print('\n knot centers:', knot_centers)
print('\n gln centers:', gln_centers)

# plot_matrix prints map after passing matrix. It has more plotting
# parameters than invariant calcluating functions, giving you more
# control over printed output.
matrix2 = plot_matrix(gln_matrix, map_arrows=False, map_cutoff=0.2,
                      map_fileformat='pdf', map_filename = 'map_gln2')
