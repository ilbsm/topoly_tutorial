from topoly import gln
from topoly.params import GlnMode, PlotFormat, test

"""
Gaussian linking number (GLN) is a measure how much two chains are
linked together. For closed chains this value take integer values i.e.
if linking happens one time, then gln equals 1 or -1, For for open chain
theres no such restriction, and value is a real number.
"""
gln = test(gln)
arc1 = 'data/arc1.xyz'
arc2 = 'data/arc2.xyz'


#===============================
# Gaussian linking number (GLN)
#===============================
print('== Gaussian linking number ==')
# Simplest usage is to calculate gln between two arcs:
full = gln(arc1, arc2)
# ...or their fragments:
fragm = gln(arc1, arc2, chain1_boundary=[3,8], chain2_boundary=[5,16])
# You can also calculate gln between two disjoint fragments of one arc:
onearc = gln(arc2, chain1_boundary=[1,8], chain2_boundary=[9,20])

print('\nGLN between full chains:', full)
print('\nGLN between subchains:', fragm)
print('\nGLN between subchains of one structure:', onearc)

# You can also find maximal absolute value of gln between all possible 
# subchains of both arcs. Paramter max_density regulates how precise the
# calculation will be. For max_density=1 all subchains are checked. For higher
# values passed to the max_density, the number of atoms will be cut and 
# analysed subsequently.

maxgln = gln(arc1, arc2, mode=GlnMode.MAX, max_density=1)
print('\nMax GLN between subchains of arc1 and subchains of arc2:', maxgln)

# Also you can find average value of gln over all possible subchains of both
# arcs:

avggln = gln(arc1, arc2, mode=GlnMode.AVG, max_density=1)
print('\nAverage GLN between subchains of arc1 and subchains of arc2:', avggln)

# If you are more interested in GLN subchain values you can use matrix mode.
# In this mode you will get GLN values between first arc and all possible 
# subchains of arc2:

matrixgln = gln(arc2, arc1, mode=GlnMode.MATRIX, matrix_plot_fname='glnmap',
                matrix_plot_format=PlotFormat.PDF)
print('\nglnmap.pdf file with gln map generated.')

# For more information about matrix manipulation check „matrices.py" file.
