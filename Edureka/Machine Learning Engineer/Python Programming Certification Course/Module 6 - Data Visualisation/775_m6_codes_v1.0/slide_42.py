import matplotlib.pyplot as plt

dictionary = {'A':25, 'B':70, 'C':55, 'D': 90}
for i, key in enumerate(dictionary):
    plt.bar(i, dictionary[key])

plt.show()
