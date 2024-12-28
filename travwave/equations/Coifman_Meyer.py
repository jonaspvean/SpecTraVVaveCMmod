from __future__ import division

from .base import Equation

class Coifman_Meyer(Equation):
    """
        The equation is :    -c*u + Lambda^s u + u * Lambda^r u = 0
    """

    def compute_kernel(self, k):
        return (1+k**2)**(self.s_fraction / 2)

    def nonlinear_kernel(self,k):
        return (1+k**2)**(self.r_fraction / 2)

    def flux(self, u):
        return u 
