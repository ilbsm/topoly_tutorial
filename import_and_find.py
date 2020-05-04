from topoly import find_loops
from topoly.params import test
"""
Topoly is flexible in accepting different file formats. Here is
practical example using find_loops as an example.

find_loops finds loops in a gives structure.
find_thetas works similarly, but finds theta-curves.
find_handcuffs too, but finds handcuffs.
"""
find_loops = test(find_loops)
f = 'data/'

#===============================
# IMPORTING STRUCTURE FROM FILE
#===============================
print('\n== Importing structure from file ==')
# You can import structures from a file. There are few accepted formats:
# pdb -- standard format for protein structure data
pdb  = find_loops(f+'1ax8.pdb')
print('pdb result:', pdb, '\n')

# cif -- standard format for crystallographic strucutre data:
cif  = find_loops(f+'1ax8.cif')
print('cif result:', cif, '\n')
cif  = find_loops(f+'1j85.cif')
print('cif result:', cif, '\n')

# xyz -- standard coordinate format with three or four columns
# three columns: x, y, z
xyz  = find_loops(f+'1ax8.xyz')
print('xyz result:', xyz, '\n')

# four columns: index, x, y, z
nxyz = find_loops(f+'1ax8.nxyz')
print('nxyz result:', nxyz, '\n')

# mathematica array format (nested curly-braced lists)
math = find_loops(f+'1ax8.math')
print('math result:', math, '\n')
math = find_loops(f+'1j85.math')
print('math result:', math, '\n')

#===================================
# IMPORTING STRUCTURE FROM VARIABLE
#==================================
print('\n\n== Importing structure from variable ==')
# here are few examples for importing from a variable:

# list of lists
lol_structure = [[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,0]]
list_of_lists = find_loops(lol_structure)
print('list-of-lists result:', list_of_lists, '\n')

# list of lists with index
lolwi_structure = [[1,0,0,0],[2,1,0,0],[3,1,1,0],[4,0,1,0],[1,0,0,0]]
list_of_lists_with_index = find_loops(lolwi_structure)
print('list-of-lists-with-index result:', list_of_lists_with_index, '\n')

# pdcode
pdcode_structure = 'V[0,1];X[5,4,3,2];X[1,0,5,2];X[3,6,7,7];X[6,8,9,9];X[8,10,11,11];X[10,4,12,12]'
pdcode = find_loops(pdcode_structure)
print('pdcode result:', pdcode, '\n')

# emcode
emcode_structure = '1V3a3b;2-3c4b7a3d;3+1V1V2a2d;4+5b2b4d4c;5+6b4a5d5c;6+7b5a6d6c;7+2c6a7d7c'
emcode = find_loops(emcode_structure)
print('pdcode result:', emcode, '\n')

