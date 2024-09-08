import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot()
data = np.random.standard_normal(30).cumsum()
ax.plot(data, color="black", label = "Default")
ax.plot(data, color ="black", linestyle="dashed", drawstyle = "steps-post", label = "steps-post")
ax.legend()
plt.show()
print("Ddsfds")