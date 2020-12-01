import mysql.connector
import csv
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database='trainning'
)

mycursor = mydb.cursor(buffered=True)

mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall()

print(tables[0])

if 'customers' not in tables[0]:
    mycursor.execute("""CREATE TABLE customers (customerid INT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), companyname VARCHAR(255)
    , billingaddress1 VARCHAR(255), billingaddress2 VARCHAR(255), city VARCHAR(255), state VARCHAR(255), postalcode VARCHAR(255), country VARCHAR(255)
    , phonenumber VARCHAR(255), emailaddress VARCHAR(255), createddate DATETIME)""")

with open('customer.csv') as csv_file:
    csv_data = csv.reader(csv_file)
    next(csv_data)
    for row in csv_data:
        row[12] += ':00'
        row[12] = datetime.strptime(row[12], '%m/%d/%Y %H:%M:%S')
        mycursor.execute("""INSERT INTO customers(customerid,firstname,lastname,companyname,billingaddress1
            ,billingaddress2,city,state,postalcode,country,phonenumber,emailaddress,createddate ) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
            row)

    mydb.commit()
    
mycursor.close()
print("Done")