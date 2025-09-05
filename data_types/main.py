import csv

data = [
    ["name", "age", "city"],
    ["John", 20, "Nairobi"],
    ["John", 20, "Nairobi"]
]

csv_file = "students.csv"
with open(csv_file, "w", newline='') as file:
    write = csv.writer(file)
    write.writerow(data)

print("students data saved to csv successfully")