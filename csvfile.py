import csv

file="hello.csv"

with open(file,"w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["name","Age","time"])

with open(file,"a",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["manha",20,"20-02-2024"])
