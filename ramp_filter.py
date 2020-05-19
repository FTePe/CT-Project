import math
import numpy as np
import numpy.matlib
from scipy.fftpack import ifft, fft, fftfreq, fftshift, ifftshift

def ramp_filter(sinogram, scale, alpha=0.001):
	""" Ram-Lak filter with raised-cosine for CT reconstruction

	fs = ramp_filter(sinogram, scale) filters the input in sinogram (angles x samples)
	using a Ram-Lak filter.

	fs = ramp_filter(sinogram, scale, alpha) can be used to modify the Ram-Lak filter by a
	cosine raised to the power given by alpha."""

	# get input dimensions
	angles = sinogram.shape[0]
	n = sinogram.shape[1]

	#Set up filter to be at least twice as long as input
	m = np.ceil(np.log(2*n-1) / np.log(2))
	m = int(2 ** m)

	
	# the Ram Lak filter
	w_max = 2*np.pi / (2*scale) # scale since that's the 'width' of the X ray beam
	# Why 2 times scale? Nyquist, to prevent aliasing
	
	#ramlak = np.abs(np.linspace(-w_max, w_max, m))
	

	filtered = np.zeros((angles, n))
	
	# implementing the filtering
	for angle in range(angles):

		signal = sinogram[angle]
		pad_len = int((m-n)*0.5)     # padding the signal

		signal = np.pad(signal, (0, 2*pad_len), constant_values = (0,0))

		f = fft(signal)
		f = fftshift(f)		# fftshift needed to centre the frequencies

		# adding a step to get the frequencies from the fft
		freqs = fftfreq(len(f))
		#freqs = freqs*(1/(2*scale))

		freqs = fftshift(freqs)
		freqs = [0 if np.abs(freq) > w_max else freq for freq in freqs]

		#f = np.multiply(f, ramlak)
		f = np.multiply(f, np.abs(freqs)/(2*np.pi))

		f = ifftshift(f)
		f = ifft(f)

		filtered[angle] = f[:-2*pad_len]	# don't consider the extra values at the end 


	sinogram = filtered
	
	return sinogram