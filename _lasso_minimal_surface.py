from topoly import lasso_type, make_surface
from topoly.params import OutputTypeLasso, PrecisionSurface, DensitySurface, SurfacePlotFormat, test

"""
Here are described method for lasso topology identification and minimal
surface generation. Topology type is based on number and direction of
tail crossings through minimal surface of lasso loop.
"""

lasso_type = test(lasso_type)
make_surface = test(make_surface)
polymer_lasso = 'newdata/lasso.xyz'
protein_lasso = 'newdata/1ax8.pdb'

#============
# LASSO TYPE
#===========
# If you want to check lasso topology type use „lasso_type" function.
# It requires a structure and its first and last indices:

polymer_lasso_type = lasso_type(polymer_lasso, [1,12])
print('.xyz structure lasso type:', polymer_lasso_type)

# If pdb file is passed without the indices, they will be imported
# from SSBOND records in pdb file:

protein_lasso_type = lasso_type(protein_lasso)
print('.pdb structure lasso type:', protein_lasso_type)

# If you check how „polymer_lasso" ('newdata/lasso.xyz') looks like
# (i.e. using xyz2pdb function) you'll realize that lasso loop is 
# crossed three times. But output is L1, which corresponds to lasso 
# crossed once. It's because of reduction of crossings. Crossing 
# reduction happens in one of three situations:
# * Two neighbouring crossings cross the minimal surface from different
#   sides. Defaultly it happens if crossings are in proximity of less  
#   than 10 atoms (aminoacids in case of proteins). 
# * Crossing is close to tail beginning. Defaultly if the distance is
#   less than 3 atoms (aminoacids).
# * Crossing is close to tail ending. Defaultly if distance is less
#   than 3 atoms (aminoacids).

# You can change these parameters using „min_dist". Defaultly 
# min_dist = [10,3,3], which refer to distance between: two crossings,
# crossing and tail beginning, crossing and tail ending.  If you do not 
# want any reduction, then use min_dist=[1,1,1]:

no_reduction = lasso_type(polymer_lasso, [1,12], min_dist=[1,1,1])
print('.xyz structure lasso type without reduction:', no_reduction)

# You can get more precise output using parameter „output_type" with
# argument „OutputTypeLasso.MoreInfo".

no_reduction = lasso_type(polymer_lasso, [1,12], min_dist=[1,1,1],
                          output_type=OutputTypeLasso.MoreInfo)
print('.xyz structure lasso type without reduction -- more info:', no_reduction)


#================
# OUTPUT QUALITY
#================
# Your output depends on quality of calculated minimal surface. You can
# control its quality using „precision", „density" and „smooth" 
# parameters. Higher precision and density gives better results but
# calculations are more time consuming. Smooth further increases 
# quality of surface. Default values: precision=PrecisionSurface.HIGH,
# density=DensitySurface.MEDIUM, smooth=0.

quality = lasso_type(polymer_lasso, [1,12], min_dist=[1,1,1],
                     precision=PrecisionSurface.HIGH,
                     density=DensitySurface.MEDIUM, smooth=0,
                     output_type=OutputTypeLasso.MoreInfo)
print('.xyz structure -- higher quality:', quality)


#==============
# SHOW SURFACE
#==============
# You can check the shape of minimal surface using „pic_files" parameter.

lasso_type(polymer_lasso, [1,12], min_dist=[1,1,1], pic_files=SurfacePlotFormat.VMD)

# Also you can just find minimal surface of chosen loop using 
# „make_surface" function.

triangles = make_surface(polymer_lasso, [1,12], precision = PrecisionSurface.LOW,
                         density=DensitySurface.LOW)
print('Minimal surface mesh coordinates:', triangles)
# Output has three levels: it is a list of dictionaries of dictionaries. 
# It is a list of triangles which build a mesh of minimal surface. Each 
# triangle is represented by a dictionary. This dictionary has triangle
# vertices as keys (with names „A", ”B", „C") and values as another dictionary.
# This last dictionary is a dictionary of space coordinates with keys „x", „y",
# „z".

