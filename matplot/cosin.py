import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0,5,0.02)
plt.plot(a, np.cos(2*np.pi*a))

plt.xlabel("time")
plt.ylabel("amplitude")
plt.title(r"cos $\mu=100$")

plt.axis([-1,6,-2,2])
plt.grid(True)
plt.show()