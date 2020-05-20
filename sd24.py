# this script checks the changes made to ct_calibrate.py
# in particular, addressing the water correction

import ct_include
from ct_include import *

#photons = source.photon('100kVp, 2mm Al')
photons = fake_source(material.mev, 1.2, coeff = None, thickness = 0, method='ideal')
n = 256
scale = 0.1
angles = 256

# ------------------------------------

# TEST 1:  Checking on 

#phantom_type = 11 # testing on a disc of tissue
phantom_type = 9 # disc made of water

phantom = ct_phantom(material.name, n, phantom_type)

# first we reconstruct the phantom WITHOUT the water calibration

sinogram1 = ct_scan(photons, material, phantom, scale, angles)
sinogram_att1 = ct_calibrate(photons, material, sinogram1, scale, correct = False)
filtered1 = ramp_filter(sinogram_att1, scale)
bp1 = back_project(filtered1)

# next we reconstruct the phantom WITH the water calibration
sinogram2 = ct_scan(photons, material, phantom, scale, angles)
sinogram_att2 = ct_calibrate(photons, material, sinogram2, scale, correct = True)
filtered2 = ramp_filter(sinogram_att2, scale)
bp2 = back_project(filtered2)

# Let us now plot a line through these reconstructions and compare the values
plt.clf()
plt.plot(bp2[127], 'y')
plt.plot(bp1[127], 'b:')
plt.xlabel('Pixel number')
plt.ylabel('Reconstructed attenuation value')
plt.legend(['With beam hardening correction', 'Without beam hardening correction'])
plt.savefig('results/week2/checking_bh_fake_single_source_water_disc_C_0_13.png', bbox_inches='tight',pad_inches = 0)
#plt.savefig('results/week2/checking_bh_real_source_tissue_disc.png', bbox_inches='tight',pad_inches = 0)
plt.show()
# RESULT: We can see that the plots overlap each other exactly, which is what we'd expect


# -------------------------------------

