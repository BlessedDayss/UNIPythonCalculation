import numpy as np
import matplotlib.pyplot as plt

family1 = np.zeros(4)
family2 = np.zeros(4)
members = np.zeros(4)

family1[:] = [1.60, 1.85, 1.75, 1.80]
family2[:] = [0.50, 0.70, 1.90, 1.75]
members[:] = [1, 2, 3, 4]
plt.plot(members, family1, 'r-', label="Family 1")
plt.plot(members, family2, 'b-', label="Family 2")

plt.xlabel("Family member number")
plt.ylabel("Height (m)")
plt.title("Family Heights Comparison")
plt.xlim(0, 5)
plt.ylim(0, 2)
plt.grid(True)
plt.legend()
plt.show()

plt.plot(members, family1, 'ro', label="Family 1 points")
plt.plot(members, family2, 'bo', label="Family 2 points")

plt.xlabel("Family member number")
plt.ylabel("Height (m)")
plt.title("Family Heights (Points Only)")
plt.xlim(0, 5)
plt.ylim(0, 2)
plt.grid(True)
plt.legend()
plt.show()