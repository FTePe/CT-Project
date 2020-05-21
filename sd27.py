import ct_include
from ct_include import *

# this script investigates the effect of low and high mas values on reconstruction

n = 256
angles = 256
scale = 0.1

#photons = source.photon('100kVp, 2mm Al')
photons = fake_source(material.mev, 1.2, coeff = None, thickness = 0, method='ideal')

ph = 6
phantom = ct_phantom(material.name, n, ph)

reconstructed1 = scan_and_reconstruct(photons, material, phantom, scale, angles, correct = True, mas = 1)
reconstructed2 = scan_and_reconstruct(photons, material, phantom, scale, angles, correct = True, mas = 100000)