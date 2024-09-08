import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

# Generate random data
data = np.random.standard_normal(30).cumsum()

# Plot data with a solid line
ax.plot(data, color="black", label="Default")

# Plot data with a dashed line and step-post style
ax.plot(data, color="black", linestyle="dashed", drawstyle="steps-post", label="steps-post")

# Add legend to the plot
ax.legend()

# Show the plot
plt.show()

# Add a simple print statement for testing
print("Plot generated and script executed successfully.")
