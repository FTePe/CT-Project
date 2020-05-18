from material import Material
import matplotlib.pyplot as plt
import numpy as np

m = Material()
# note: m.mev is the energies (in MeV) for which attenuation values for different materials is available

#print(len(m.mev))
#print(len(m.coeff('Blood')))

name = 'Soft Tissue'

compton = np.reciprocal(m.mev)
photo = np.reciprocal((np.power(m.mev, 3)))

plt.plot(m.mev, m.coeff(name))
plt.plot(m.mev, compton, 'y')
plt.plot(m.mev, photo, 'r')
plt.legend([name, 'Compton', 'Photoelectric'])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Energy (log scale)')
plt.ylabel('Attenuation (log scale)')
plt.show()


x_mev = m.mev[:-1]
plt.plot(x_mev, np.diff(np.log(m.coeff(name))))
plt.plot(x_mev, np.diff(np.log(compton)), 'y')
plt.plot(x_mev, np.diff(np.log(photo)), 'r')
plt.legend([name, 'Compton', 'Photoelectric'])
plt.xscale('log')
#plt.yscale('log')
plt.xlabel('Energy (log scale)')
plt.ylabel('Attenuation (first derivative of log)')
plt.show()
