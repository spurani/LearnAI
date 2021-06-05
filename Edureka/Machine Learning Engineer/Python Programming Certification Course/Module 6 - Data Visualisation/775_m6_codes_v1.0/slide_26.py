import matplotlib.pyplot as plt
x =range(5)
plt.plot(x, [x1 for x1 in x], x, [x1*2 for x1 in x], x, [x1*4 for x1 in x])
plt.grid(True)
plt.xlim(-1, 5)
plt.ylim(-1, 10)
plt.show()