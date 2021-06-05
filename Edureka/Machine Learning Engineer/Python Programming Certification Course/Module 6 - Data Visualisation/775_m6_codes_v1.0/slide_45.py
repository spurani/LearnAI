import matplotlib.pyplot as plt
plt.figure(figsize=(3,3))
x = [40, 20, 5]
labels = ['Bikes', 'Cars', 'Buses']
plt.pie(x, labels=labels)
plt.show()