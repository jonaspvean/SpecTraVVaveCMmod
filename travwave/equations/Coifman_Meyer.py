from __future__ import division

from .base import Equation
import numpy as np

class Coifman_Meyer(Equation):
    """
        The equation is :    -c*u + Lambda^s u + u * Lambda^r u = 0
    """

    def compute_kernel(self, k):
        return (1+k**2)**(self.s_fraction / 2)

    def nonlinear_kernel(self,k):
        return (1+k**2)**(self.r_fraction / 2)

        '''
        if k[0] == 0:
            k1 = k[1:]
            return np.concatenate(([0],(abs(k1))**(self.r_fraction)))
        else:
            return (abs(k))**(self.r_fraction )
        '''
    def flux(self, u):
        return u 
