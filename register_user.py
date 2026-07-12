import csv
import os

file_name = "users.csv"

if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["User ID", "Name"])

user_id = input("Enter User ID: ")
name = input("Enter User Name: ")

with open(file_name, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([user_id, name])

print("User Registered Successfully!")