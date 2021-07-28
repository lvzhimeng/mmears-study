import pandas as pd
import numpy as np
'''值计数（直方图）与众数'''
#统计每个数出现的次数，即值计数
data = np.random.randint(0,7,size=50)
print()
print(pd.value_counts(data))
#出现最多的数即众数
s = pd.Series(data)
print(s.mode())
