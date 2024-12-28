import numpy as np

from travwave.diagram import BifurcationDiagram
import travwave.equations as teq
import travwave.boundary as tbc

import matplotlib.pyplot as plt

length = np.pi
s_fraction = -0.50
r_fraction = -0.30
isCM = True

equation = teq.Coifman_Meyer.Coifman_Meyer(length, s_fraction, r_fraction, isCM)


boundary_cond = tbc.Const()


# constructing the bifuraction diagram
bd = BifurcationDiagram(equation, boundary_cond, size=512, criticality=1.0, use_mode = 'Lambda_r')
# initialize it with default parameters
bd.initialize()
# run for a certain number of steps - has to be varied in order to reach a highest wave
bd.navigation.run(385)


print('Amplitude = ', bd.navigation[-1]['parameter'][bd.navigation.amplitude_])
print('Max of Lambda^r = ', bd.navigation[-1]['lambda_r'])


new_size = 1028
refined, v, parameter, _ = bd.navigation.refine_at(new_size)

bd.plot_solution(refined)
plt.show()

bd.plot_diagram()
#plt.plot(parameter[0], parameter[1], 'or')
plt.show()








