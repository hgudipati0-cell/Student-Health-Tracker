import pandas as pd

data = pd.read_csv("data.csv")

#determine the averages of each criteria 
print("\nAverage hours of sleep:")
print(data["sleep"].astype(float).mean())

print("\nAverage study hours:")
print(data["study"].astype(float).mean())

print("\nAverage mood:")
print(data["mood"].astype(float).mean())

#determining the correlation of the data
print(data.corr(numeric_only=True))