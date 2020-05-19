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
	
	filtered = np.zeros((angles, n))
	
	# implementing the filtering
	for angle in range(angles):

		signal = sinogram[angle]

		# STEP 1: Pad the signal to match the filter length
		pad_len = int((m-n)*0.5)     # padding the signal
		signal = np.pad(signal, (0, 2*pad_len), constant_values = (0,0))

		# STEP 2: Calculate fft of the signal, and shift the coefficients to zero-centre them
		f = fft(signal)

		# STEP 3: Calculate frequencies from length of signal, and scale them 
		freqs = fftfreq(len(f))
		freqs = freqs*(1/(scale))

		freqs[0] = freqs[1]/6  # the approximate correction

		# STEP 4: Element wise multiplication of the FFT and the Ram lak filter 
		f = np.multiply(f, np.abs(freqs))

		# STEP 5: Shift back to get the zeroeth element at the start of the array, then iFFT
		f = ifft(f)

		# STEP 6: extract the required signal values (remove the padding's effect)
		filtered[angle] = f[:-2*pad_len]	# don't consider the extra values at the end 


	sinogram = filtered
	
	return sinogram