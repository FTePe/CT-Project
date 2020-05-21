import ct_include
from ct_include import *

photons = source.photon('100kVp, 2mm Al')
#photons = fake_source(material.mev, 1.2, coeff = None, thickness = 0, method='ideal')
n_array = [128, 512]
scale = 0.1



angles_array = np.array([30, 90, 150, 210, 270])

for i in range(len(angles_array)):
    phantom = ct_phantom(material.name, n_array[0], 7)
    reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles_array[i],\
         do_mas = False, correct = False, do_noise = False, do_hu = False)
    plt.clf()
    plt.axis('off')
    plt.imshow(reconstructed, cmap = 'gray', vmin = 0, vmax = 0.3*np.amax(reconstructed))
    plt.savefig('results/week2/filter/varying_with_angles_size_128_%d'%(angles_array[i]), bbox_inches='tight',pad_inches = 0)

for i in range(len(angles_array)):
    phantom = ct_phantom(material.name, n_array[1], 7)
    reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles_array[i],\
         do_mas = False, correct = False, do_noise = False, do_hu = False)
    plt.clf()
    plt.axis('off')
    plt.imshow(reconstructed, cmap = 'gray', vmin = 0, vmax = 0.3*np.amax(reconstructed))
    plt.savefig('results/week2/filter/varying_with_angles_size_512_%d'%(angles_array[i]), bbox_inches='tight',pad_inches = 0)