import matplotlib.pyplot as plt

import csv
import numpy as np

# a = np.zeros((3,3))

# b = np.ones((3,3))

# c = np.array([[1,2],[2,3]])
# print(c.shape)
# print(b)

# x = np.linspace(0, 2 * np.pi, 1000)
# y = np.sin(x)
# plt.figure()
# plt.plot(x, y)
# plt.show()

x = np.linspace(0, 10, 100000)

y = np.sin(x)

z = y + (np.random.rand(100000) - 0.5) * 0.1

error = z - y

error = np.sqrt(error**2)

error_sum = np.sum(error)

print(error_sum)

plt.figure()
plt.plot(x, y)
plt.plot(x, z)
plt.plot(x, error)
plt.show()

