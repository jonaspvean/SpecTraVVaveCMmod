
import numpy as np

from travwave.diagram import BifurcationDiagram
import travwave.equations as teq
import travwave.boundary as tbc

import matplotlib.pyplot as plt

# here, length is the half-period
length = np.pi
s_fraction = -0.50


# s_fraction takes care of the fractional exponent
equation = teq.fKdV.fKdV(length, s_fraction)

# the case when B = 0:
boundary_cond = tbc.Const()

bd = BifurcationDiagram(equation, boundary_cond, size=516, criticality = 1.0)
# initialize it with default parameters
bd.initialize()
# run for a certain number of steps - has to be varied in order to reach a highest wave
bd.navigation.run(210)


print('Amplitude = ', bd.navigation[-1]['parameter'][bd.navigation.amplitude_])
#print(bd.navigation[-1]['solution'][0] - bd.navigation[-1]['solution'][-1])

# refinement
new_size = 1028
refined, v, parameter, _ = bd.navigation.refine_at(new_size)


bd.plot_solution(bd.navigation[-1]['solution'])
bd.plot_solution(refined)
plt.show()


bd.plot_diagram()
#plt.plot(parameter[0], parameter[1], 'or')
plt.show()

