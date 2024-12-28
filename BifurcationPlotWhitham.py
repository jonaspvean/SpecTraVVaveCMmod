import numpy as np

from travwave.diagram import BifurcationDiagram
import travwave.equations as teq
import travwave.boundary as tbc

import matplotlib.pyplot as plt

length = np.pi

equation = teq.whitham.Whitham(length)

boundary_cond = tbc.Const()

bd = BifurcationDiagram(equation, boundary_cond, size=516, criticality=0.66)
# initialize it with default parameters
bd.initialize()
# run for a certain number of steps - has to be varied in order to reach a highest wave
bd.navigation.run(150)

print('Amplitude = ', bd.navigation[-1]['parameter'][bd.navigation.amplitude_])
print('Max value = ', bd.navigation[-1]['maximum'])
print('Max of Lambda^r = ', bd.navigation[-1]['lambda_r'])

# refinement
new_size = 1028
refined, v, parameter, _ = bd.navigation.refine_at(new_size)


#bd.plot_solution(bd.navigation[-1]['solution'])
bd.plot_solutions()
plt.show()


bd.plot_diagram()
#plt.plot(parameter[0], parameter[1], 'or')
plt.show()



