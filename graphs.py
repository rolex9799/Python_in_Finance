
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show(block=False)
input('press <ENTER> to continue')


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show(block=False)
input('press <Enter> to continue')
