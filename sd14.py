import ct_include
from ct_include import *

# This script investigates the sinogram of a phantom while changing the default interpolation method
photons = source.photon('100kVp, 2mm Al')
n = 256
scale = 0.1
angles = 256

phantom_type = 2


phantom = ct_phantom(material.name, n, phantom_type)
scan = ct_scan(photons, material, phantom, scale, angles)
sinogram = ct_calibrate(photons, material, scan, scale, correct = False)





