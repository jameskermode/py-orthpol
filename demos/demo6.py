"""
Same as demo1.py, but generates the Legendre polynomials.

This demo demonstrates how to:
    + Construct a set of orthogonal univariate polynomials given a weight
      function.
    + Examine certain properties of a univariate polynomial.
    + Evaluate the polynomials at one or more points.
    + Evaluate the derivatives of the polynomials at one or more points.

Author:
    Ilias Bilionis

Date:
    3/18/2014
"""


import orthpol
import math
import numpy as np
import matplotlib.pyplot as plt


# The desired degree
degree = 4

# The first way of doing it is by directly supplying the weight function
wf = lambda x: 1.
# Construct it:
p = orthpol.OrthogonalPolynomial(degree,
                                left=0., right=1., # Domain
                                wf=wf)
# An orthogonal polynomial is though of as a function.
# Here is how to get the number of inputs and outputs of that function
print('Number of inputs:', p.num_input)
print('Number of outputs:', p.num_output)
# Test if the polynomials are normalized (i.e., their norm is 1.):
print('Is normalized:', p.is_normalized)
# Get the degree of the polynomial:
print('Polynomial degree:', p.degree)
# Get the alpha-beta recursion coefficients:
print('Alpha:', p.alpha)
print('Beta:', p.beta)
# The following should print a description of the polynomial
print(str(p))
# Now you can evaluate the polynomial at any points you want:
X = np.linspace(0., 1., 100)
# Here is the actual evaluation
phi = p(X)
# Phi should be a 100x11 matrix: phi(i, j) = poly(i, X[j])
# Let's plot them
plt.plot(X, phi)
plt.title('Legendre Polynomials', fontsize=16)
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$p_i(x)$', fontsize=16)
plt.legend(['$p_{%d}(x)$' % i for i in range(p.num_output)], loc='best')
print('Close the window to continue...')
plt.show()
# You may also compute the derivatives of the polynomials:
dphi = p.d(X)
# Let's plot them also
plt.plot(X, dphi)
plt.title('Derivatives of Legendre Polynomials', fontsize=16)
plt.xlabel('$x$', fontsize=16)
plt.ylabel(r'$\frac{dp_i(x)}{dx}$', fontsize=16)
plt.legend([r'$\frac{p_{%d}(x)}{dx}$' % i for i in range(p.num_output)], loc='best')
print('Close the window to end demo...')
plt.show()
