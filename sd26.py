import ct_include
from ct_include import *

# this script checks the effect of reconstructions (without any water correction)
# on an anatomical phantom using real and ideal single energy sources

n = 256
angles = 256
scale = 0.1

photons1 = source.photon('100kVp, 2mm Al')
photons2 = fake_source(material.mev, 1.2, coeff = None, thickness = 0, method='ideal')

ph = 6
phantom = ct_phantom(material.name, n, ph)

reconstructed1 = scan_and_reconstruct(photons1, material, phantom, scale, angles, correct = False, do_mas = False)
reconstructed2 = scan_and_reconstruct(photons2, material, phantom, scale, angles, correct = False, do_mas = False)

plt.clf()

plt.axis('off')
f1 = plt.imshow(reconstructed1, cmap = 'gray')
plt.tight_layout()
plt.savefig('results/week2/real_phantom_6_no_water_correction_.png', bbox_inches='tight',pad_inches = 0)

plt.axis('off')
f2 = plt.imshow(reconstructed2, cmap = 'gray')
plt.tight_layout()
plt.savefig('results/week2/fake_phantom_6_no_water_correction_.png', bbox_inches='tight',pad_inches = 0)