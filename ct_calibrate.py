import numpy as np
import scipy
from scipy import interpolate
import math
from ct_detect import ct_detect

def ct_calibrate(photons, material, sinogram, scale, correct=True):

	""" ct_calibrate convert CT detections to linearised attenuation
	sinogram = ct_calibrate(photons, material, sinogram, scale) takes the CT detection sinogram
	in x (angles x samples) and returns a linear attenuation sinogram
	(angles x samples). photons is the source energy distribution, material is the
	material structure containing names, linear attenuation coefficients and
	energies in mev, and scale is the size of each pixel in x, in cm."""

	# ct_calibrate(source.photon('100kVp, 2mm Al'), material, scan, 0.1

	# Get dimensions and work out detection for just air of twice the side
	# length (has to be the same as in ct_scan.py)
	n = sinogram.shape[1]

	# getting the intensity value for a phantom of just air along any angle
	value = ct_detect(photons, material.coeff('Air'), 2*n*scale, 1)[0]

	 # getting the linear attenuated sinogram as per the formula
	sinogram = sinogram/value
	sinogram = -np.log(sinogram)

	# perform calibration

	return sinogram