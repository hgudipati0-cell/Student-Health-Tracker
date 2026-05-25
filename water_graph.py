import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.plot(data["water"].astype(float))

plt.title("Liters of water drank over time")
plt.xlabel("Entry number")
plt.ylabel("Litres of water")

plt.show()