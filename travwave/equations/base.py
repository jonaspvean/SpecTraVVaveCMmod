#!/usr/bin/env python
# coding: utf-8
from __future__ import division

import numpy as np

class Equation(object):
    def __init__(self, length=np.pi, s_fraction = -0.5, r_fraction = -0.5, isCM = False):
        self.s_fraction = s_fraction
        self.r_fraction = r_fraction
        self.length = length
        self.isCM = isCM

    def compute_kernel(self, k, s_fraction, r_fraction):
        raise NotImplementedError()

    def flux(self, u):
        raise NotImplementedError()

    