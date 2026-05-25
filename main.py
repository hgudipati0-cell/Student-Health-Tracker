import csv
import os
from datetime import date

file_exists = os.path.isfile("data.csv")

today = date.today()

sleep = input("Hours slept: ")
water = input("Liters of water drank: ")
study = input("Hours studied: ")
mood = input("Mood out of 10: ")

data = [today, sleep, water, study, mood]

with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["date", "sleep", "water", "study", "mood"])

    writer.writerow(data)

print("Data saved successfully!")
