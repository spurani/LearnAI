import numpy, matplotlib.pyplot as plt
x = numpy.arange(0, 5, 0.01)
plt.plot(x, [x1**2 for x1 in x])
plt.show()