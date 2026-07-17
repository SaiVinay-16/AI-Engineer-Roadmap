import csv
with open("data_1.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name", "Age", "Branch"])
    writer.writerow(["Alice", 20, "CSE"])
    writer.writerow(["Bob", 21, "IT"])