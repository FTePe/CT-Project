from ct_include import *
import ct_include

# This script investigates the effect of varying the number of angles on the reconstructed image

# this fake source should give us a single energy source at 0.2 MeV
#photons = fake_source(material.mev, 1.2, coeff = None, thickness = 0, method='ideal')
photons = source.photon('100kVp, 2mm Al')

n = 256
scale = 0.1
angles = np.linspace(60, 300, 6)

phantom_type = 6
phantom = ct_phantom(material.name, n, phantom_type)

centre_line = np.zeros((len(angles), n))

for i in range(len(angles)):

    sinogram = ct_scan(photons, material, phantom, scale, np.int(angles[i]))
    sinogram_att = ct_calibrate(photons, material, sinogram, scale)
    filtered = ramp_filter(sinogram_att, scale)
    bp = back_project(filtered)

    centre_line[i] = bp[127]

# now to create the plot of centre lines
for i in range(len(angles)):
    plt.plot(centre_line[i])
plt.legend(angles)
plt.xlabel('Pixel number')
plt.ylabel('Attenuation value')
plt.savefig('results/week2/varying_with_angles.png', bbox_inches='tight',pad_inches = 0)

    

