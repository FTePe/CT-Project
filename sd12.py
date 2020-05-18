from ct_include import *
import ct_include

# define the range of depths
depths = np.arange(0, 10.1, 0.1)

# -------------------------------------------------

# TASK 1: Real source

# define the energy source of photons 
photons = source.photon('100kVp, 2mm Al')

y1 = ct_detect(photons, material.coeff('Water'), depths, 1)
plt.plot(np.log(y1), 'y') # this gives a straight line

y2 = ct_detect(photons, material.coeff('Bone'), depths, 1)
plt.plot(np.log(y2), 'r') # this gives a straight line

y3 = ct_detect(photons, material.coeff('Titanium'), depths, 1)
plt.plot(np.log(y3), 'k') # this gives a straight line

plt.xlabel('Depth (cm)')
plt.ylabel('Residual intensity value')
plt.legend(['Water', 'Bone', 'Titanium'])

plt.savefig('results/week1.real_source_attenuation.png')

plt.show()

# -------------------------------------------------

# TASK 2: Fake source

# define the energy source of photons 
photons = fake_source(material.mev, 1.2, material.coeff('Aluminium'), thickness=2, method='ideal')

y1 = ct_detect(photons, material.coeff('Water'), depths, 1)
plt.plot(np.log(y1), 'y') # this gives a straight line

y2 = ct_detect(photons, material.coeff('Bone'), depths, 1)
plt.plot(np.log(y2), 'r') # this gives a straight line

y3 = ct_detect(photons, material.coeff('Titanium'), depths, 1)
plt.plot(np.log(y3), 'k') # this gives a straight line

plt.xlabel('Depth (cm)')
plt.ylabel('Residual intensity value')
plt.legend(['Water', 'Bone', 'Titanium'])

plt.savefig('results/week1.fake_source_attenuation.png')

plt.show()