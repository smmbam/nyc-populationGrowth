import pandas as pd
from matplotlib import pyplot as plt

# Command Line Data Display
# df = pd.read_csv('nyc_PopulationGrowth.csv', index_col = 0)
# df = df[df.columns[0:2]]
# print(df.to_string())
# print("Total number of Years: ", len(df.columns[0]))


# Hypothesis
# Does New York City's population increase over a long period of time?

# Reads CSV File
df = pd.read_csv('nyc_PopulationGrowth.csv')

# Designates Columns w/ axis
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Bar Graph Customs
plt.bar(X, Y, color='g')
plt.title("NYC Population Growth")
plt.xlabel("Year")
plt.ylabel("Population")

# Shows the Plot
plt.show()
