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

# If you check how „polymer_lasso" ('newdata/lasso.xyz') look like
# (for example using xyz2pdb) you'll realize that lasso loop is crossed
# three times, but gained topology type: L1 is lasso with one crossing.
# It's because of reduction of crossings which are neighbouring and have
# opposite sign. Crossings are also reduced when they are close to tail 
# beginning or end. 

# You can change these parameters using „min_dist". Defaultly 
# min_dist = [10,3,3], which means that crossings which are closer than 
# 10 atoms (aminoacids in proteins) or closer than 3 atoms (aminoacids) 
# to tail beginning or end are reduced. If you do not want any
# reduction, then use min_dist=[1,1,1]:

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




















