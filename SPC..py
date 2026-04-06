import numpy as np
import matplotlib.pyplot as plt

# Sample data: 10 subgroups, each with 5 measurements (mm)
data = np.array([
    [20.02, 19.98, 20.01, 20.03, 19.99],
    [20.05, 20.04, 20.02, 20.01, 20.03],
    [19.97, 19.96, 19.98, 19.99, 19.95],
    [20.10, 20.08, 20.09, 20.11, 20.07],
    [20.00, 20.02, 19.99, 20.01, 20.03],
    [19.94, 19.96, 19.95, 19.97, 19.93],
    [20.06, 20.07, 20.05, 20.04, 20.08],
    [20.03, 20.02, 20.01, 20.04, 20.00],
    [19.92, 19.91, 19.93, 19.94, 19.90],
    [20.05, 20.06, 20.04, 20.07, 20.03]
])

# Constants for n=5
A2 = 0.577
D3 = 0
D4 = 2.114

means = data.mean(axis=1)
ranges = data.max(axis=1) - data.min(axis=1)

X_bar = means.mean()
R_bar = ranges.mean()

UCLx = X_bar + A2 * R_bar
LCLx = X_bar - A2 * R_bar
UCLr = D4 * R_bar
LCLr = D3 * R_bar

# Plot X-bar chart
plt.figure()
plt.plot(means, marker='o')
plt.axhline(UCLx)
plt.axhline(X_bar)
plt.axhline(LCLx)
plt.title("X-bar Chart")
plt.xlabel("Sample")
plt.ylabel("Mean Diameter (mm)")
plt.show()

# Plot R chart
plt.figure()
plt.plot(ranges, marker='o')
plt.axhline(UCLr)
plt.axhline(R_bar)
plt.axhline(LCLr)
plt.title("R Chart")
plt.xlabel("Sample")
plt.ylabel("Range (mm)")
plt.show()
