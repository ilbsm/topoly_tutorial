import urllib.request
from topoly import import_coords, alexander, plot_matrix

# downloading the PDB structure and keeping it in the variable "data"
fp = urllib.request.urlopen("https://files.rcsb.org/view/1J85.pdb")
data_bytes = fp.read()
data = data_bytes.decode("utf8")
fp.close()

# parsing the coordinates to required format
curve = import_coords(data)

# analysis of the whole chain using the Alexander polynomial with two-point closure
print(alexander(curve, closure_method='two_points', translate=True))

# analysis of the whole chain using the Alexander polynomial with closed by rays, 100 times
print(alexander(curve, closure_method='rays', tries=100, translate=True))

# analysis of the subchains and present it as a matrix
matrix = alexander(curve, matrix=True, closure_method='two_points', translate=True)

# plotting the matrix and storing it as 'my_matrix.svg'
plot_matrix(matrix, plot_ofile='my_matrix', plot_format='svg')



