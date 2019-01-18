from pandas import read_csv
import pandas as pd
import matplotlib.pyplot as plt

# Get data
Location = r"G:\Python\Env\pm_project\static\contratos_2018.csv"
df = pd.read_csv(Location, header=None)

# Create graph
plt.plot(df[0], df[1])
plt.show()

