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

	# Get dimensions and work out detection for just air of twice the side
	# length (has to be the same as in ct_scan.py)
	n = sinogram.shape[1]


	# FIRST: Calibrate for air, convert intensity values to measured attenuation

	# getting the intensity value for a phantom of just air along any angle
	value = ct_detect(photons, material.coeff('Air'), 2*n*scale, 1)[0]

	 # getting the linear attenuated sinogram as per the formula
	sinogram = sinogram/value
	sinogram = -np.log(sinogram)

	"""
	# SECOND: Calibrate for water
	f = water_f(photons, material, n, scale, deg = 3)
	p = np.poly1d(f)

	t_wm = p(sinogram)   # this is for all sinogram attenuation values
	C = 1		# Scaling factor
	mu_c = C*t_wm

	sinogram = mu_c
	"""
	

	return sinogram

def water_f(photons, material, side_length, scale, deg):

	t = np.linspace(scale, side_length*np.sqrt(2)*scale, 100)

	#mu_w = ct_detect(photons, material.coeff('Water'), t)  # note! This gives only the intensity

	I_tot = ct_detect(photons, material.coeff('Water'), t) # recorded intensity
	# getting the intensity value for a phantom of just air along any angle
	value = ct_detect(photons, material.coeff('Air'), 2*side_length*scale, 1)[0]
	I = I_tot/value
	mu_w = -np.log(I)

	f = np.polyfit(mu_w, t, deg)

	return f