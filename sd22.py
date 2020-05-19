from ct_include import *
import ct_include

photons = source.photon('100kVp, 2mm Al')
n = 256
scale = 0.1
angles = 180

# -------------------------------------

# TASK 1: Calculate the impulse response of the Ramlak filter

phantom = ct_phantom(material.name, n, 2)
reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles)

# -------------------------------------

# TASK 2: Scanning and reconstructing some phantoms

ph_type = [1, 3]
for ph in ph_type:
    phantom = ct_phantom(material.name, n, ph) # disc
    reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles)
    save_draw(reconstructed, 'results/week2', 'filtered_ph_%d.png' % (ph))
