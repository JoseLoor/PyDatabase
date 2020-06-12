import os

import mysql.connector
import pandas as pd
from dotenv import load_dotenv
from mysql.connector import errorcode

load_dotenv()

data = pd.read_csv("test_dataset_for_yahia.csv")

mydb = mysql.connector.connect(host=os.getenv("DB_HOST"),   
                                user=os.getenv("DB_USER"),   
                                passwd=os.getenv("DB_PASSWORD"),
                                 database = os.getenv("DB_DATABASE"),
                                auth_plugin=os.getenv("DB_AUTHPLUGIN"))  

print(mydb)


# print(data["experiment"][0])

# checkIfExists = f"""IF EXISTS (SELECT* FROM INFORMATION_SCHEMA.TABLES
#                 WHERE size = )
#     BEGIN
#         drop table test3
#     END
#     """

# checkIfExists = f"""IF EXISTS (SELECT* FROM INFORMATION_SCHEMA.TABLES)
#     BEGIN
#         drop table test3
#     END
                    
#     ELSE 
                    
#     BEGIN
#         CREATE TABLE excelnellie.test3 (
#     {data.columns[0]} varchar(50),
#     {data.columns[1]} varchar(50),
#     {data.columns[2]} varchar(50),
#     {data.columns[3]} varchar(50),
#     {data.columns[4]} varchar(50),
#     {data.columns[5]} varchar(50),
#     {data.columns[6]} varchar(50),
#     {data.columns[7]} varchar(50)
# );"""

# createTable = f"""CREATE TABLE excelnellie.test3 (
#     {data.columns[0]} varchar(50),
#     {data.columns[1]} varchar(50),
#     {data.columns[2]} varchar(50),
#     {data.columns[3]} varchar(50),
#     {data.columns[4]} varchar(50),
#     {data.columns[5]} varchar(50),
#     {data.columns[6]} varchar(50),
#     {data.columns[7]} varchar(50)
# );"""

value = "INSERT INTO excelnellie.test1 (combo) values (9)"

mycursor = mydb.cursor()
mycursor.execute(value)
mydb.commit()

result=mycursor.execute("select * from excelnellie.test1")

for row in mycursor.fetchall():
    print (row)

mycursor.close()
mydb.close()

# def insertData(mydb, params):
#     mycursor = mydb.cursor()
#     mycursor.execute(f"INSERT INTO excelnellie.test1 (combo) values ({params[1]})")
#     mydb.commit()

# for row in range(10):
#     tempList = []
#     for columns in data.columns:
#         tempList.append(data[columns][row])
#     # print(tempList)
#     insertData(mydb, tempList)

# mycursor = mydb.cursor()

# mycursor.execute(checkIfExists)

# print (data.loc[0,:])
