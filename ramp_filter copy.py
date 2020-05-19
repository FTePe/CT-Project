"""

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

	w_max = 2*np.pi / (2*scale) # scale since that's the 'width' of the X ray beam
	
	filtered = np.zeros((angles, n))
	
	# implementing the filtering
	for angle in range(angles):

		signal = sinogram[angle]

		# STEP 1: Pad the signal to match the filter length
		pad_len = int((m-n)*0.5)     # padding the signal
		signal = np.pad(signal, (0, 2*pad_len), constant_values = (0,0))

		# STEP 2: Calculate fft of the signal, and shift the coefficients to zero-centre them
		f = fft(signal)
		#f = fftshift(f)		# fftshift needed to centre the frequencies

		# STEP 3: Calculate frequencies from length of signal, and scale them 
		freqs = fftfreq(len(f))
		#freqs = freqs*(1/(2*scale))   # since 1/2*scale is the 'sampling frequency'  # don't need 2  
		freqs = freqs*(1/(scale))
		
		# now need to shift the frequencies to zero-centre them
		#freqs = fftshift(freqs)
		# and set all frequencies above w_max to zero
		#freqs = [0 if np.abs(freq) > w_max else freq for freq in freqs]  # don't need

		freqs[0] = freqs[1]/6  # the approximate correction

		# STEP 4: Element wise multiplication of the FFT and the Ram lak filter
		#f = np.multiply(f, np.abs(freqs)/(2*np.pi))   # don't need the 2pi factor - since we already got the frequency in Hz
		f = np.multiply(f, np.abs(freqs))

		# STEP 5: Shift back to get the zeroeth element at the start of the array, then iFFT
		#f = ifftshift(f)
		f = ifft(f)

		# STEP 6: extract the required signal values (remove the padding's effect)
		filtered[angle] = f[:-2*pad_len]	# don't consider the extra values at the end 


	sinogram = filtered
	
	return sinogram

"""