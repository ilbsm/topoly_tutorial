from topoly import *

# importing the file 31.xyz. It is closed knot.
curve = 'data/31.xyz'

polynomials = {}
# calculating the polynomials
polynomials['Alexander'] = alexander(curve, closure=Closure.CLOSED, poly_reduce=True)
polynomials['Conway'] = conway(curve, closure=Closure.CLOSED, poly_reduce=True)
polynomials['Jones'] = jones(curve, closure=Closure.CLOSED, poly_reduce=True)
polynomials['HOMFLY-PT'] = homfly(curve, closure=Closure.CLOSED, poly_reduce=True)
polynomials['Kauffman bracket'] = kauffman_bracket(curve, closure=Closure.CLOSED, poly_reduce=True)
polynomials['Kauffman polynomial'] = kauffman_polynomial(curve, closure=Closure.CLOSED, poly_reduce=True)
polynomials['BLM/Ho'] = blmho(curve, closure=Closure.CLOSED, poly_reduce=True)
polynomials['Yamada'] = yamada(curve, closure=Closure.CLOSED, poly_reduce=True)

# Printing the polynomials and matching knot from the dictionary. We need the short version of the polynomial
print("Knot polynomials for the 3_1 knot:")
for key in polynomials.keys():
    print(key, polynomials[key], find_matching(polynomials[key].print_short()))

