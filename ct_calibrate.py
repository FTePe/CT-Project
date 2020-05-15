import numpy as np
import scipy
from scipy import interpolate
import sys
from ct_detect import ct_detect
import math
from attenuate import attenuate

def ct_calibrate(photons, material, sinogram, scale, correct=True):

	""" ct_calibrate convert CT detections to linearised attenuation
	sinogram = ct_calibrate(photons, material, sinogram, scale) takes the CT detection sinogram
	in x (angles x samples) and returns a linear attenuation sinogram
	(angles x samples). photons is the source energy distribution, material is the
	material structure containing names, linear attenuation coefficients and
	energies in mev, and scale is the size of each pixel in x, in cm."""

	# Get dimensions and work out detection for just air of twice the side
	# length (has to be the same as in ct_scan.py)
	angles = sinogram.shape[0]
	n = sinogram.shape[1]
	xi, yi = np.meshgrid(np.arange(n) - (n/2) + 0.5, np.arange(n) - (n/2) + 0.5)


	scan = np.zeros((angles, n))
	for angle in range(angles):

		sys.stdout.write("Calibrating angle: %d   \r" % (angle + 1) )

		# Get rotated coordinates for interpolation
		p = -math.pi / 2 - angle * math.pi / angles
		x0 = xi * math.cos(p) - yi * math.sin(p) + (n/2) - 0.5
		y0 = xi * math.sin(p) + yi * math.cos(p) + (n/2) - 0.5

		# For each material, add up how many pixels contain this on each ray
		depth = np.zeros((len(material.coeffs), n))

		interpolated = scipy.ndimage.map_coordinates(np.ones((n,n)), [y0, x0], order=1, mode='constant', cval=0, prefilter=False)
		
		# only necessary for more complex forms of interpolation above
		# depth = np.clip(depth, 0, None)

		# ensure an appropriate amount of air is included in the calculation
		# to account for the scan being circular, but the phantom being square
		# diameter of circle taken to be twice the phantom side length
		depth = 2 * n - np.sum(interpolated, axis=0)
		# scale the depth appropriately and calculate detections for this set of
		# materials
		depth*= scale
		print(depth)

		scan[angle] = ct_detect(photons, material.coeff('Air'), depth, 1)# - this is correct 
	
	# perform calibration
	sinogram = -np.log( np.divide(scan, sinogram))

	return sinogram