from __future__ import division

from .base import Equation

class fKdV(Equation):
    """
    The equation is :    -c u + Lambda^s u + 1/2 u^2 = 0
    """

    def compute_kernel(self, k):
        return (1+k**2)**(self.s_fraction / 2)

    def flux(self, u):
        return 0.5*u*u
    
    def nonlinear_kernel(self, k):
        return 0