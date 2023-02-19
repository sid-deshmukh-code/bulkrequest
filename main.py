import csv

with open('top500Domains.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
