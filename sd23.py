# this script tries to understand the hu.py function

import ct_include
from ct_include import *

photons = source.photon('100kVp, 2mm Al')
n = 256
scale = 0.1
angles = 180

# ------------------------------------

phantom = ct_phantom(material.name, n, 6)

# create sinogram from phantom data, with received detector values
sinogram = ct_scan(photons, material, phantom, scale, angles)

# convert detector values into calibrated attenuation values
sinogram_att = ct_calibrate(photons, material, sinogram, scale)

# Ram-Lak
filtered = ramp_filter(sinogram_att, scale)

# Back-projection
bp = back_project(filtered)

# convert to Hounsfield Units
bp_hu = hu(photons, material, bp, scale)