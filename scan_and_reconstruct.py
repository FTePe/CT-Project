from ct_scan import *
from ct_calibrate import *
from ct_lib import *
from ramp_filter import *
from back_project import *
from hu import *

def scan_and_reconstruct(photons, material, phantom, scale, angles, mas=10000, alpha=0.001, \
	do_filtering = True, do_mas = True, correct = True, do_hu = True, do_noise = True):

	""" Simulation of the CT scanning process
		reconstruction = scan_and_reconstruct(photons, material, phantom, scale, angles, mas, alpha)
		takes the phantom data in phantom (samples x samples), scans it using the
		source photons and material information given, as well as the scale (in cm),
		number of angles, time-current product in mas, and raised-cosine power
		alpha for filtering. The output reconstruction is the same size as phantom."""


	# convert source (photons per (mas, cm^2)) to photons 
	if(do_mas==True):
		print("do_mas true!")
		photons = (photons*mas)*(scale**2)

	# create sinogram from phantom data, with received detector values
	sinogram = ct_scan(photons, material, phantom, scale, angles, mas, do_noise)

	# convert detector values into calibrated attenuation values
	sinogram_att = ct_calibrate(photons, material, sinogram, scale, correct)

	# Filtering
	if(do_filtering==True):
		filtered = ramp_filter(sinogram_att, scale)
		sinogram_att = filtered
	
	
	bp = back_project(sinogram_att)

	# Back-projection
	

	# convert to Hounsfield Units
	
	#bp_hu = hu(photons, material, bp, scale)

	#phantom = bp_hu
	phantom = bp

	return phantom