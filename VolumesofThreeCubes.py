import numpy as np
import matplotlib.pyplot as plt

L = np.linspace(1, 3, 3)
print("L values:", L)

V_manual = L**3
print("Manual V values:", V_manual)

V = L ** 3
print("Program output V:", V)

plt.plot(L, V, marker='o', linestyle='-', color='blue')
plt.xlabel("L (cm)")
plt.ylabel("Volume V (cm³)")
plt.title("Volume of Cube vs Side Length")
plt.grid(True)
plt.show()