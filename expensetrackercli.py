"""
expense tracker with csv where total presented yearly and each year expense can be checked using cli
"""
import csv
import argparse
import datetime
file="customers.csv"
years={}
parser=argparse.ArgumentParser(description="total yearly expenses")
parser.add_argument("--year",type=str)

args=parser.parse_args()
with open(file,"r",newline="") as f:#open file to read
    reader=csv.DictReader(f) #read the csv
    for row in reader: #check each row eg: {time:20, age:20}
        year=row["time"].split("-")[-1] #to get only the year
        amount=float(row["amount"]) #to get the amount in the row amount
        if year not in years: #checks if the given year in list
            years[year]=0 #initialized value of the item in year to zero
        years[year]+=amount #adds value to it
    if args.year:
        if args.year in years:
            print(f"year {args.year}: total:{years[args.year]}")
        else:
            print("error")
    else:
        for year,total in years.items(): #to print the total of each year
         print(f"year {year}: total:{total}")
