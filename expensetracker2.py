"""
looks through a manually created csv and returns the total from each year
"""
import csv

file="customers.csv"
years={}

with open(file,"r",newline="") as f:#open file to read
    reader=csv.DictReader(f) #read the csv
    for row in reader: #check each row eg: {time:20, age:20}
        year=row["time"].split("-")[-1] #to get only the year
        amount=float(row["amount"]) #to get the amount in the row amount
        if year not in years: #checks if the given year in list
            years[year]=0 #initialized value of the item in year to zero
            years[year]+=amount #adds value to it
    for year,total in years.items(): #to print the total of each year
     print(f"year {year}: total:{total}")


