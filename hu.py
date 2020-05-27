import numpy as np
from attenuate import *
from ct_scan import *
from ct_calibrate import *
from ramp_filter import *
from back_project import *
from ct_phantom import *

def hu(p, material, reconstruction, scale):
	""" convert CT reconstruction output to Hounsfield Units
	calibrated = hu(p, material, reconstruction, scale) converts the reconstruction into Hounsfield
	Units, using the material coefficients, photon energy p and scale given."""
	
	n = reconstruction.shape[0]
	#angles = 180

	# use water to calibrate
	# calibration done by using a n x n phantom made of water
	#phantom_water = ct_phantom(material.name, n, 10)

	# put this through the same calibration process as the normal CT data
	#sinogram = ct_scan(p, material, phantom_water, scale, angles)
	#sinogram_att = ct_calibrate(p, material, sinogram, scale)
	#filtered = ramp_filter(sinogram_att, scale)
	#reconstruction_water = back_project(filtered)

	#mu_w = ct_detect(p, material.coeff('Water'), n*scale, do_noise = False)
	#mu_w = 0.137 # random value taken from the mass_attenuation excel sheet
	mu_w = 0.206 # this value for the Xtreme scanner, since peak energy is lower

	# use result to convert to hounsfield units
	reconstruction_hu = reconstruction - mu_w
	reconstruction_hu = np.divide(reconstruction_hu, mu_w)*1000

	reconstruction = reconstruction_hu

	# limit minimum to -1024, which is normal for CT data.
	# setting the lower and the upper bounds for HU
	reconstruction = np.clip(reconstruction, -1024, 3072)

	"""
	All this is done in the viewer
	-------------------------------

	# converting HU to appropriate pixel values
	c = 0
	w = 200
	
	g = reconstruction - c
	g = np.divide(g, w)
	g=g*128+128

	# is this step needed? Otherwise there is possibility for g to be greater than 255
	# interpolate into [0, 255] range rather than clip
	g_min = np.amin(g)
	g_max = np.amax(g)
	g = np.divide(g-g_min, g_max-g_min)*(255)+0
	#g = np.clip(g, 0, 255)

	reconstruction = g
	"""

	return reconstruction