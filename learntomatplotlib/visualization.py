# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# The plot method on Series and DataFrame is just a simple wrapper around plt.plot():
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
# ts.plot()
# plt.show()

# If the index consists of dates, it calls gcf().autofmt_xdate() to try to format the x-axis nicely as per above.
# 可以简便的将所有列绘制出来
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
# plt.figure(); df.plot();
# plt.show()

#可以指定一个列数据类x轴
df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df3['A'] = pd.Series(list(range(len(df))))
df3.plot(x='A', y='B')
plt.show()

#其他各种图形见 http://pandas.pydata.org/pandas-docs/stable/visualization.html#visualization
