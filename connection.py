#Libraries
import csv
import MySQLdb 
import sys

#Connecting to a MySQL database
#Connection credentials used will work only if you are connected over VPN. Create your setup and replace values for connection,

class MySQLConnection:
    con = MySQLdb.connect(host='your_host', 
                          port=3306, 
                          user='your_username',
                          database='nyc_restaurants',
                          passwd='your_password')
    c = con.cursor()
    
    # Get the count
    main_query = c.execute('''SELECT count(CAMIS) FROM DOHMH_New_York_City_Restaurant_Inspection_Results''')
    # If the count is 1, then customers_dataset table already exists
    row = c.fetchone()
    if row != None : {
        print('Connection successfull and records already exist.')
    }
    else: 
        # Load data from csv to db format
        c.execute('''LOAD DATA INFILE '/var/lib/mysql/DOHMH_New_York_City_Restaurant_Inspection_Results.csv'
        INTO TABLE `DOHMH_New_York_City_Restaurant_Inspection_Results`
        FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
        IGNORE 1 ROWS;''')
        print('Table created.')
