import numpy as np
import matplotlib.pyplot as plt

# Generate a sample dataset of ages
np.random.seed(0)
ages = np.random.randint(18, 80, size=1000)

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=15, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
