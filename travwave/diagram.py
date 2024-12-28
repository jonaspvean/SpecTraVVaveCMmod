from __future__ import division

from travwave import navigation, solver, discretization

import numpy as np
import matplotlib.pyplot as plt

class BifurcationDiagram(object):

    def __init__(self, equation, boundary_condition, size=32, init_size=256, criticality=1.0, use_mode = 'Wave max'):
        self.discretization = discretization.Discretization(equation, init_size)
        solve = solver.Solver(self.discretization, boundary=boundary_condition)
        nav = navigation.Navigator(solve.solve, size=size)
        self.navigation = nav
        self.criticality = criticality
        self.use_mode = use_mode

    def initialize(self, amplitude=0.01, step=0.005):
        initial_guess = self.discretization.compute_initial_guess(amplitude)
        initial_velocity = self.discretization.bifurcation_velocity()
        p0 = (initial_velocity, 0)
        base = (initial_velocity, step)
        self.navigation.initialize(initial_guess, p0, base)

    def plot_data_wave_amp(self):
        parameters = [result['parameter'] for result in self.navigation]
        aparameters = np.array(parameters)
        return aparameters.T

    def plot_data_wave_max(self):
        parameters = [[result['parameter'][self.navigation.velocity_], result['maximum']] for result in self.navigation]
        aparameters = np.array(parameters)
        return aparameters.T
    
    def plot_data_lambda_r(self):
        parameters = [[result['parameter'][self.navigation.velocity_], result['lambda_r']] for result in self.navigation]
        aparameters = np.array(parameters)
        return aparameters.T

    def plot_diagram(self):
        if self.use_mode == 'Wave max':
            # uses the maximum value compared against the wave speed
            aparameters = self.plot_data_wave_max()
            plt.plot(aparameters[0], aparameters[1], '.--')
            plt.xlabel('Wavespeed')
            x = np.linspace(0, 1, 1000)
            y = self.criticality*x
            plt.plot(x, y, linestyle='-')  # solid
            plt.ylabel('Waveheight')

        if self.use_mode == 'Lambda_r':
            # uses the maximum of Lambda^r u compared against the wave speed
            aparameters = self.plot_data_lambda_r()
            plt.plot(aparameters[0], aparameters[1], '.--')
            plt.xlabel('Wavespeed')
            x = np.linspace(0, 1, 1000)
            y = self.criticality*x
            plt.plot(x, y, linestyle='-')  # solid
            plt.ylabel('Waveheight')

        if self.use_mode == 'Amplitude':
            # uses the total height of the wave compared against the wave speed
            aparameters = self.plot_data_wave_amp()
            plt.plot(aparameters[0], aparameters[1], '.--')
            plt.xlabel('Wavespeed')
            x = np.linspace(0, 1, 1000)
            y = self.criticality*x
            plt.plot(x, y, linestyle='-')  # solid
            plt.ylabel('Waveheight')
        
    def plot_solution(self, solution):
        size = len(solution)
        nodes = discretization.get_nodes(size, self.discretization.equation.length)
        plt.plot(nodes, solution)
        plt.xlabel('x')
        plt.ylabel('Surface Elevation')
        
    def plot_solutions(self, index = [-1]):
        counter = np.arange(np.size(index))
        for i in counter:
            solution = self.navigation[index[i]]['solution']
            self.plot_solution(solution)
