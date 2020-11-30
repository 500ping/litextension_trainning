import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database='trainning'
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")


if 'customers' not in mycursor:
    mycursor.execute("""CREATE TABLE customers (customerid INT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), companyname VARCHAR(255)
    , billingaddress1 VARCHAR(255), billingaddress2 VARCHAR(255), city VARCHAR(255), state VARCHAR(255), postalcode VARCHAR(255), country VARCHAR(255)
    , phonenumber VARCHAR(255), emailaddress VARCHAR(255), createddate VARCHAR(255))""")

with open('customer.csv') as csv_file:
    csv_data = csv.reader(csv_file)
    next(csv_data)
    for row in csv_data:
        row[12] += ':00'
        mycursor.execute("""INSERT INTO customers(customerid,firstname,lastname,companyname,billingaddress1
            ,billingaddress2,city,state,postalcode,country,phonenumber,emailaddress,createddate ) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
            row)

    mydb.commit()
    
mycursor.close()
print("Done")