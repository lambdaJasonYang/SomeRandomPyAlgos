import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
# activate plot theme
import qeds
qeds.themes.mpl_style();
# Step 1
fig, ax = plt.subplots()

# Step 2
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Step 3
ax.plot(x, y)

plt.show()
