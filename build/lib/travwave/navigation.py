from __future__ import division

from .discretization import resample

def ortho_direction(p, base):
    """
    Returns the orthogonal direction to (base - p)
        pstar = p2 + step*(p2-p1)
    """
    dp = (base[0] - p[0], base[1] - p[1])
    direction = (-dp[1], dp[0])
    return direction

class Navigator(object):
    """
    Runs the iterator and stores the result.
    """

    def __init__(self, solve, size=32):
        """
        solve: solve function
        size: size for the navigation
        """
        self.solve = solve
        self.size = size

    # the indices for velocity and amplitude
    velocity_, amplitude_ = (0, 1)

    def __getitem__(self, index):
        return self._stored_values[index]

    def __len__(self):
        return len(self._stored_values)

    def initialize (self, current, p, base):
        """
        Creates a list for solutions and stores the first solution (initial guess).
        """
        self._stored_values = []
        variables = [0]
        self._stored_values.append({'solution': resample(current, self.size), 'integration constant': variables, 'parameter': p, 'base': base})

    def compute_direction(self, p1, p2):
        """
        Strategy for a new parameter direction search.
        """
        return ortho_direction(p1, p2)

    def run(self, N):
        """
        Iterates the solver N times, navigating over the bifurcation branch and storing found solutions.
        """
        for i in range(N):
            self.step()

    def two_parameter_points(self, index):
        p2 = self[index]['parameter']
        p1 = self[index-1]['parameter']
        return p2, p1

    def run_solver(self, current, pstar, direction):
        new, variables, p3 = self.solve(current, pstar, direction)
        return new, variables, p3

    def refine(self, resampling, sol, p, direction):
        """
        Refine from solution `sol` at parameter `p` in direction `direction` in the parameter space.
        """
        sol_ = resample(sol, resampling)
        new, variables, p_ = self.run_solver(sol_, p, direction)
        return new, variables, p_

    def refine_at(self, resampling, index=-1):
        """
        Refine using a direction orthogonal to the last two parameter points.
        """
        p2, p1 = self.two_parameter_points(index)
        dir = self.compute_direction(p2, p1)
        current = self[index]['solution']
        return self.refine(resampling, current, p2, dir)

    def step(self):
        p = self[-1]['parameter']
        base = self[-1]['base']
        direction = self.compute_direction(p, base)
        current = self[-1]['solution']
        new, variables, p_ = self.run_solver(current, base, direction)
        dp = (p_[0] - p[0], p_[1] - p[1])
        pstar = (p_[0] + dp[0], p_[1] + dp[1])
        self._stored_values.append({'solution': new, 'integration constant': variables, 'parameter': p_, 'base': pstar})

