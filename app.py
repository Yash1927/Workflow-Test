import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

# Generating data
data = np.random.standard_normal(30).cumsum()

# Plot with incorrect parameters (e.g., an undefined color)
ax.plot(data, color="undefined-color", label="Error")

ax.legend()
plt.show()
print(hyyy)