import json
import csv
import requests
def start():
    csvfile = open('sample.csv', 'w')
    writer = csv.writer(name.csv, delimiter=',')
    writer.writerow(
        ["bhk_details", "house_type", "latitude", "longitude", "Inventory", "shared", "private", "rent",
         "advance", "city"])
    for i in range(1, 800):
        start_url = 'https://www.bangalore.com&order_by=&page=' + str(i) + 'XXXXXXXXXX'
headers = {'content-type': 'application/json',
                   'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:62.0) Gecko/20100101 Firefox/62.0"}
        data = requests.get(url=start_url, headers=headers).json()
for object in data['houses']:
            writer.writerow([object['bhk_details'], object['house_type'], object['latitude'], object['longitude'],
                             object['Inventory'], object['shared'], object['private'], object['rent'],
                             object['advance'],object['city']])