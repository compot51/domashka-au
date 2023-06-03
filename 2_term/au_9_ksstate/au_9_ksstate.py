import pandas
import numpy
import matplotlib.pyplot as plt
from scipy import stats

df = pandas.read_csv("monte_py.csv")

# df['experiments'].plot(kind="bar")

# df['experiments'].plot.kde()
# plt.show()

# print(df.experiments.describe())

print(stats.kstest(df['experiments'], 'norm', (df['experiments'].mean(), df['experiments'].std()), N=5000))
