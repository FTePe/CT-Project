from ct_include import *
import ct_include

# this fake source should give us a single energy source at 0.2 MeV
photons = fake_source(material.mev, 1.2, coeff = None, thickness = 0, method='ideal')

n = 256
scale = 0.1
angles = 256

# use the simple disc phantom
phantom = ct_phantom(material.name, n, 1)

sinogram = ct_scan(photons, material, phantom, scale, angles)

sinogram_att = ct_calibrate(photons, material, sinogram, scale)

filtered = ramp_filter(sinogram_att, scale)

bp = back_project(filtered)

plt.plot(bp[127])
plt.show()

