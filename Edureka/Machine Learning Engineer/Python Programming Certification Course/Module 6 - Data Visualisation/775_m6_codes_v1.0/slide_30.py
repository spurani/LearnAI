import matplotlib.pyplot as plt
x =range(5)
plt.plot(x, [x1 for x1 in x], x, [x1*2 for x1 in x], x, [x1*4 for x1 in x])
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Polynomial Graph')
plt.show()