import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1, 3, 0.2)
plt.plot(y, '*', y+0.5, 'o', y+1, 'D', y+2, '^', y+3, 's')
plt.show()