import csv

with open('top500Domains.csv', 'r') as file:
    reader = csv.reader(file)
    

    web_list = []


    for row in reader:
        web_list.append(row[1])


print(web_list)

        
        

    

#----------------------------------------------------------

