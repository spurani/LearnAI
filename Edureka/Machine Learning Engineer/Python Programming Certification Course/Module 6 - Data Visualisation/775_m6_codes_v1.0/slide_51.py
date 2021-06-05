import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1, 100)
plt.plot(y, '--', y*5, '-.', y*10, ':')
plt.show()

