import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# this program extract some basic features of the data
# helps to have more understanding of the data

data = pd.read_csv('ac_cleaned.csv')
print(data)
# count the number of products of each brand
brands = []
count = []
for row in data['Brand']:
    if row not in brands:
        brands.append(row)
        count.append(1)
    else:
        count[brands.index(row)] += 1
plt.bar(brands, count)
plt.xticks(np.arange(len(brands)), brands, rotation=90)
for i in range(len(brands)):
    plt.text(i, count[i]+1, count[i], ha='center', va='bottom', fontsize=7)
plt.show()

# the mean of C_Power energy consume
# (the electrical power used by the unit(kW) at 35 degrees C working at full load)
print("Average Full Load Cooling Energy Consume:")
print(str(data['C-Power_Inp_Rated'].mean()) + " kW/h")

# the mean of H_Power energy consume
# (the electrical power used by the unit(kW) at 7 degrees C working at full load)
print("Average Full Load Heating Energy Consume:")
print(str(data['H-Power_Inp_Rated'].mean()) + " kW/h")