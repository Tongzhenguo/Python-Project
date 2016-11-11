import numpy as np
import pandas as pd
## load csv to numpy array
tmp = np.loadtxt("F:\code\Python-Project\dataset\\tags1.dat", dtype=np.str, delimiter="::")
# print tmp
df = pd.DataFrame(tmp, columns=["uid", "vid", "rating", "timestamp"])
# print df

###overall popularity :users count for ratings[i]
overall_popularity = df.groupby(by=["rating"])["uid"].count()
print overall_popularity

##local popularity:users count for videos[i] and ratings[j]
local_popularity = df.groupby(["vid","rating"])["uid"].count()
print local_popularity
