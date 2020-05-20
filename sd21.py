from ct_include import *
import ct_include


photons = source.photon('100kVp, 2mm Al')
n = 256
scale = 0.1
angles = 180

#phantom = ct_phantom(material.name, n, 1)
#reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles, mas=10000, alpha=0.001)

ph_type = [1, 2]

# ------------------------------------------------------

# TASK 1
# Experimenting with scan_and_reconstruct WITHOUT and WITH the filtering step for phantom 
# type 1 and 2. For this, we just reproduce the scan_and_reconstruct code below.

plt.clf()
for ph in ph_type:

    phantom = ct_phantom(material.name, n, ph)
    sinogram = ct_scan(photons, material, phantom, scale, angles)
    sinogram_att = ct_calibrate(photons, material, sinogram, scale, correct = False) # correct is water correction
    filtered = ramp_filter(sinogram_att, scale)

    bp_without = back_project(sinogram_att)
    bp_with = back_project(filtered)

    fig, axarr = plt.subplots(1,3)
    axarr[0].axis('off')
    axarr[1].axis('off')
    axarr[2].axis('off')
    f1 = axarr[0].imshow(phantom, cmap = 'gray')
    f2 = axarr[1].imshow(bp_without, cmap = 'gray')
    f3 = axarr[2].imshow(bp_with, cmap = 'gray')
    fig.tight_layout()
    plt.savefig('results/week2/check_filter_reconstruct_%d.png' % (ph), bbox_inches='tight',pad_inches = 0)

# ------------------------------------------------------------------
plt.clf()

# TASK 2 (EXPERIMENTing)
# Doing the same thing as before, but this time looking at the sinogram
# of a complex phantom

ph = 6 # complex phantom
angles = 256

phantom = ct_phantom(material.name, n, ph)
sinogram = ct_scan(photons, material, phantom, scale, angles)
sinogram_att = ct_calibrate(photons, material, sinogram, scale, correct = False) # correct is water correction
filtered = ramp_filter(sinogram_att, scale)

fig, axarr = plt.subplots(1,2)
axarr[0].axis('off')
axarr[1].axis('off')
f1 = axarr[0].imshow(sinogram_att, cmap = 'gray')
f2 = axarr[1].imshow(filtered, cmap = 'gray')
fig.tight_layout()
plt.savefig('results/week2/check_filter_reconstruct_sinograms_phantom_%d.png' % (ph), bbox_inches='tight',pad_inches = 0)




