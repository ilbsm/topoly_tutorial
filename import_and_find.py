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

#=====================
# IMPORTING FROM FILE
#=====================
# You can import structures from a file. There are few accepted formats:
# pdb -- standard format for protein structure data
pdb  = find_loops(f+'1ax8.pdb')
print('pdb result:', pdb)

# cif -- standard format for crystallographic strucutre data:
cif  = find_loops(f+'1ax8.cif')
print('cif result:', cif)

# xyz -- standard coordinate format with three or four columns
# three columns: x, y, z
xyz  = find_loops(f+'1ax8.xyz')
print('xyz result:', xyz)

# four columns: index, x, y, z
nxyz = find_loops(f+'1ax8.nxyz')
print('nxyz result:', nxyz)

# mathematica array format (nested curly-braced lists)
math = find_loops(f+'1ax8.math')
print('math result:', math)

#=========================
# IMPORTING FORM VARIABLE
#=========================
# here are few examples for importing from a variable:

# list of lists
lol_structure = [[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,0]]
list_of_lists = find_loops(lol_structure)
print('list-of-lists result:', list_of_lists)

# list of lists with index
lolwi_structure = [[1,0,0,0],[2,1,0,0],[3,1,1,0],[4,0,1,0],[1,0,0,0]]
list_of_lists_with_index = find_loops(lolwi_structure)
print('list-of-lists-with-index result:', list_of_lists_with_index)

# pdcode
pdcode_structure = None
pdcode = find_loops(pdcode_structure)
print('pdcode result:', pdcode)

# emcode
emcode_structure = None
emcode = find_loops(emcode_structure)
print('pdcode result:', emcode)

