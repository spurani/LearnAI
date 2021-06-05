import matplotlib.pyplot as plt
x =range(5)
plt.plot(x, [x1 for x1 in x], x,
         [x1*x1 for x1 in x], x, [x1*x1*x1 for x1 in x])
plt.show()