import pylab as plt
import numpy as np

Z = np.random.random((500,500))   # Test data
plt.imshow(Z, cmap='gray', interpolation='nearest')
plt.show()