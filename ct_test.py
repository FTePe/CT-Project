
# these are the imports you are likely to need
import numpy as np
from material import *
from source import *
from fake_source import *
from ct_phantom import *
from ct_lib import *
from scan_and_reconstruct import *
from create_dicom import *

# create object instances
material = Material()
source = Source()

# define each end-to-end test here, including comments
# these are just some examples to get you started
# all the output should be saved in a 'results' directory

def test_1():
	# For this test, view the plots and compare visually that they have similar geometry

	# work out what the initial conditions should be
	p = ct_phantom(material.name, 256, 3)
	s = source.photon('100kVp, 3mm Al')
	y = scan_and_reconstruct(s, material, p, 0.01, 256)

	# save some meaningful results
	save_draw(y, 'results', 'test_1_image')
	save_draw(p, 'results', 'test_1_phantom')
	plt.close()

def test_2():
	# This test compares the data values on the 128th row of the phantom and the
	# reconstructed image for the point impulse phantom

	# work out what the initial conditions should be
	p = ct_phantom(material.name, 256, 2)
	s = source.photon('80kVp, 1mm Al')
	y = scan_and_reconstruct(s, material, p, 0.01, 256)

	# save some meaningful results
	#save_plot(y[128,:], 'results', 'test_2_plot')
	
	plt.plot(y[127, :])
	plt.plot(p[127, :])
	plt.title('Comparing the data values on the 128th row')
	plt.legend(['Reconstruced', 'Phantom'])
	plt.ylabel('Data value')
	plt.xlabel('Sample')
	#plt.show()
	plt.savefig('results/test_2_plot')
	plt.close()


def test_3():
	# This test compares the mean value of the central area of pixels between the 
	# phantom and the reconstructed image for the point impule phantom

	# work out what the initial conditions should be
	p = ct_phantom(material.name, 256, 1)
	s = fake_source(source.mev, 0.1, method='ideal')
	y = scan_and_reconstruct(s, material, p, 0.1, 256)

	# save some meaningful results
	f = open('results/test_3_output.txt', mode='w')
	f.write('Mean value is of middle part of reconstructed is ' + str(np.mean(y[64:192, 64:192])))
	f.write("\n")
	f.write('Mean value is of middle part of phantom is ' + str(np.mean(p[64:192, 64:192])))
	f.close()


def test_4():
	# This test compares the data values for the phantom and reconstructed image across 
	# the 128th row of pixels - type 6 phantom

	# work out what the initial conditions should be
	p = ct_phantom(material.name, 256, 6)
	s = source.photon('80kVp, 2mm Al')
	y = scan_and_reconstruct(s, material, p, 0.01, 256)

	# save some meaningful results

	# let's compare the values when we scale to the same range
	y_scaled = y[127, :]
	y_scaled = np.interp(y_scaled, (y_scaled.min(), y_scaled.max()), (-1, +10))

	p_scaled = p[127, :]
	p_scaled = np.interp(p_scaled, (p_scaled.min(), p_scaled.max()), (-1, +10))
	
	plt.plot(y_scaled)
	plt.plot(p_scaled)
	plt.title('Comparing the data values on the 128th row - Scaled')
	plt.legend(['Reconstruced', 'Phantom'])
	plt.ylabel('Data value')
	plt.xlabel('Sample')
	#plt.show()
	plt.savefig('results/test_4_plot_scaled')
	plt.close()


# Run the various tests
print('Test 1')
test_1()
print('Test 2')
test_2()
print('Test 3')
test_3()
print('Test 4')
test_4()
