from ct_include import *
import ct_include


photons = source.photon('100kVp, 2mm Al')
n = 256
scale = 0.1
angles = 180

#phantom = ct_phantom(material.name, n, 1)
#reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles, mas=10000, alpha=0.001)

# ------------------------------------------------------

# TASK 1
# Experimenting with scan_and_reconstruct without the filtering step for phantom 
# type 1 and 2. For this, we just reproduce the scan_and_reconstruct code below.

ph_type = [1, 2]

for ph in ph_type:

    phantom = ct_phantom(material.name, n, ph)
    sinogram = ct_scan(photons, material, phantom, scale, angles)
    sinogram_att = ct_calibrate(photons, material, sinogram, scale)
    # no filtering step
    bp = back_project(sinogram_att)

	# convert to Hounsfield Units
	#bp_hu = hu(photons, material, bp, scale)       # this was not done at the time!

    fig, axarr = plt.subplots(1,2)

    f1 = axarr[0].imshow(phantom, cmap = 'gray')
    #plt.colorbar(f1, ax = f1, orientation='vertical')
    plt.axis('off')

    f2 = axarr[1].imshow(bp, cmap = 'gray')
    #plt.colorbar(f2, ax = f1, orientation='vertical')
    plt.axis('off')

    fig.tight_layout()

    plt.savefig('results/week2/no_filter_reconstruct_%d.png' % (ph))


