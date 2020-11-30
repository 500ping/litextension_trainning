import requests
import json
import csv

res = requests.get('https://b6bfa186a8b9767d75c8bd4d114ff950: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@500ping.myshopify.com/admin/api/2020-10/customers.json')

customers_data = json.loads(res.text)
# print(customers_data)

customers = []

for customer in customers_data['customers']:
    customer.pop('addresses', None)
    customer.pop('default_address', None)
    customers.append(customer)

csv_columns = list(customers[0].keys())
print(csv_columns)

with open('customers.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for data in customers:
        writer.writerow(data)