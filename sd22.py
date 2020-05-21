from ct_include import *
import ct_include

photons = source.photon('100kVp, 2mm Al')
n = 256
scale = 0.01
angles = 256

# -------------------------------------

# TASK 1: Calculate the impulse response of the Ramlak filter

#phantom = ct_phantom(material.name, n, 2)
#reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles)

# -------------------------------------

# TASK 2: Scanning and reconstructing some phantoms

phantom = ct_phantom(material.name, n, 6) 
reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles, correct = False,\
    do_mas = False, do_noise=False, do_filtering=True)
    
plt.clf()
plt.axis('off')
plt.imshow(reconstructed, cmap = 'gray')
plt.savefig('results/week2/filtered_no_corrections_ph_6', bbox_inches='tight',pad_inches = 0)