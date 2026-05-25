import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.plot(data['sleep'].astype(float))

plt.title("Hours of sleep over time")
plt.xlabel("Entry number")
plt.ylabel("Hours slept")

plt.show()

