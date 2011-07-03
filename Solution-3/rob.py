import math

# global storage for values x_i
xi = {}

# function returning length of chord x_i:
# (keep in mind: range(i, j) returns values [i, j[ )
def fxi( i, c, d ):
	# return stored value if already computed:
	if xi.has_key( i ):
		return xi[ i ]
	# case i = 1: x_1 = c - 1
	if i == 1:
		xi[ i ] = c - 1.0
	# other x_i
	else:
		# calculate recursive formula as given in paper:
		xi[ i ] = ( c *
		            (1.0 + d * math.sin( math.fsum( [ math.asin( fxi( j, c, d ) / d ) for j in range( 1, i ) ] ) )
		            )
		            - i
		            - math.fsum( [ fxi( j, c, d ) for j in range( 1, i ) ] )
		          )
	# if reaching negative values:
	if xi[ i ] < 0:
		del xi[ i ] # delete cached (negative) value
		raise RuntimeError # raise an error
	return xi[ i ] # return valid x_i

# function returning length of chord connecting end point of x_i and starting point:
def dxi( i, c, d ):
	return d * math.sin(
	                    math.fsum( [ math.asin( fxi( j, c, d ) / d ) for j in range( 1, i + 1 ) ] )
	                   )

def printXi( i, c, d ):
	for i in range( 1, i + 1 ):
		try:
			print 'x_%d = %.16f' % ( i, fxi( i, c, d ) )
		except RuntimeError:
			print 'Aborted.'

