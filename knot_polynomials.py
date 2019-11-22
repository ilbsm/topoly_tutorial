from topoly import *

# importing the file 31.xyz. It is closed knot.
curve = import_coords('31.xyz')

polynomials = {}
# calculating the polynomials
polynomials['Alexander'] = alexander(curve, closure_method='closed', poly_reduce=False)
polynomials['Conway'] = conway(curve, closure_method='closed', poly_reduce=False)
polynomials['Jones'] = jones(curve, closure_method='closed', poly_reduce=False)
polynomials['HOMFLY-PT'] = homfly(curve, closure_method='closed', poly_reduce=False)
polynomials['Kauffman bracket'] = kauffman_bracket(curve, closure_method='closed', poly_reduce=False)
polynomials['Kauffman polynomial'] = kauffman_polynomial(curve, closure_method='closed', poly_reduce=False)
polynomials['BLM/Ho'] = blmho(curve, closure_method='closed', poly_reduce=False)
polynomials['Yamada'] = yamada(curve, closure_method='closed', poly_reduce=False)

# Printing the polynomials and matching knot from the dictionary. We need the short version of the polynomial
print("Knot polynomials for the 3_1 knot:")
for key in polynomials.keys():
    print(key, polynomials[key], find_matching(polynomials[key].print_short()))

