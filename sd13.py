import ct_include
from ct_include import *

photons = source.photon('100kVp, 2mm Al')
n = 256
scale = 0.1
angles = 180

# ----------------------

# TASK 1: Investigate what sinogram obtained from ct_scan looks like for various
# simple shapes and complex ones.
print('Task 1 started')

# single point
phantom = ct_phantom(material.name, n, 2)
scan = ct_scan(photons, material, phantom, scale, angles)
save_draw(scan, 'results/week1', 'single_point_centre')

# single point but offset
# this was done in ipython since I didn't want to change any parameters for ct_phantom
# Done by editing the ct_phantom case 1 code, and then running this script

# disc
phantom = ct_phantom(material.name, n, 1)
scan = ct_scan(photons, material, phantom, scale, angles)
save_draw(scan, 'results/week1', 'simple_disc')

# case 5 - bilateral hip replacement
phantom = ct_phantom(material.name, n, 5)
scan = ct_scan(photons, material, phantom, scale, angles)
save_draw(scan, 'results/week1', 'bilateral_hip_replacement')

print('Task 1 done')

# ----------------------

# TASK 2: Varying the number of angles
# case 7 - pelvic fixation pins
print('Task 2 started')

angles_array = [30, 90, 150, 210, 270]
for angles in angles_array:
    phantom = ct_phantom(material.name, n, 7)
    scan = ct_scan(photons, material, phantom, scale, angles)
    save_draw(scan, 'results/week1', 'angles_num_%d' % (angles))

print('Task 2 done')

# ----------------------

# TASK 3: Varying the default interpolation method

