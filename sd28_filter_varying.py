import ct_include
from ct_include import *

photons = source.photon('100kVp, 2mm Al')
#photons = fake_source(material.mev, 1.2, coeff = None, thickness = 0, method='ideal')
n = 256
scale = 0.1

phantom = ct_phantom(material.name, n, 7)

angles_array = np.array([30, 90, 150, 210, 270])
for i in range(len(angles_array)):
    reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles_array[i],\
         do_mas = False, correct = False, do_noise = False, do_hu = False)
    plt.clf()
    plt.axis('off')
    plt.imshow(reconstructed, cmap = 'gray', vmin = 0, vmax = 0.3*np.amax(reconstructed))
    plt.savefig('results/week2/filter/varying_with_angles_%d'%(angles_array[i]), bbox_inches='tight',pad_inches = 0)
    