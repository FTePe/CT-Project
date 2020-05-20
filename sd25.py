import ct_include
from ct_include import *

# This script aims to investigate CT noise 

#photons = source.photon('100kVp, 2mm Al')
photons = fake_source(material.mev, 1.2, coeff = None, thickness = 0, method='ideal')
scale = 0.1
mas = 10000
n = 256
angles = 256

phantom_type = 4

phantom = ct_phantom(material.name, n, phantom_type)

reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles, mas)
