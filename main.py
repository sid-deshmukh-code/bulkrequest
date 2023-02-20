import csv
import requests
count = 0
with open('top500Domains.csv', 'r') as file:
    reader = csv.reader(file)
    

    web_list = []

    # getting list of top 500 websites from 
    for row in reader:
        web_list.append(row[1])

web_list.pop(0)
print(web_list)


for webs in web_list:
    try:
        response = requests.get(f"https://{webs}")
        print(f"{webs}-----------{response.status_code}")
        
    except:
        count += 1
        continue


print(f"Errors: {count}")

        
        

    



