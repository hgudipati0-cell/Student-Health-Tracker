import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.plot(data["study"].astype(float))

plt.title("Hours studied over time")
plt.xlabel("Entry number")
plt.ylabel("Hours studied")

plt.show()