# this script tries to understand the hu.py function

import ct_include
from ct_include import *

photons = source.photon('100kVp, 2mm Al')
#photons = fake_source(material.mev, 1.2, coeff = None, thickness = 0, method='ideal')
n = 256
scale = 0.1
angles = 256

# ------------------------------------

phantom_type = 10

phantom = ct_phantom(material.name, n, phantom_type)
sinogram = ct_scan(photons, material, phantom, scale, angles)
sinogram_att = ct_calibrate(photons, material, sinogram, scale, correct = False)
filtered = ramp_filter(sinogram_att, scale)
bp = back_project(filtered)

# convert to Hounsfield Units
#bp_hu = hu(photons, material, bp, scale)

# -------------------------------------

