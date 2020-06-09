import numpy as np
import matplotlib.pyplot as plt


theta = np.linspace(0, 2*np.pi, 1000)

r = np.sqrt(1.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

# fig, ax = plt.subplots(1)

# ax.plot(x1,x2)
# ax.set_aspect(1)
plt.plot(x1, x2)
plt.show()