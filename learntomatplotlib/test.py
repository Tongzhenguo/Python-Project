import matplotlib.pylab as plt
import numpy as np
import pandas as pd

y = np.arange(100)
plt.plot(y)
plt.show()

df = pd.DataFrame(y)
df.plot()
plt.plot(df)
plt.show()