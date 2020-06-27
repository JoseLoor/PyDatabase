import os

import mysql.connector
import pandas as pd
from dotenv import load_dotenv
from mysql.connector import errorcode

data = pd.read_csv("test_dataset_for_yahia.csv") # CSV where we are getting the data

headerList = ['index', 
        data.columns[0],
        data.columns[1],
        data.columns[2],
        data.columns[3],
        data.columns[4],
        data.columns[5],
        data.columns[6],
        data.columns[7],
        data.columns[8],
        data.columns[9],
        data.columns[10],
        data.columns[11],
        data.columns[12],
        data.columns[13],
        data.columns[14],
        data.columns[15],
        data.columns[16],
        data.columns[17],
        data.columns[18],
        data.columns[19],
        data.columns[20],
        data.columns[21],
        data.columns[22],
        data.columns[23],
        data.columns[24],
        data.columns[25],
        data.columns[26],
        data.columns[27],
        data.columns[28],
        data.columns[29],
        data.columns[30],
        data.columns[31],
        data.columns[32],
        data.columns[33],
        data.columns[34],
        data.columns[35],
        data.columns[36],
        data.columns[37],
        data.columns[38],
        data.columns[39],
        data.columns[40],
        data.columns[41],
        data.columns[42],
        data.columns[43],
        data.columns[44],
        data.columns[45],
        data.columns[46],
        data.columns[47],
        data.columns[48],
        data.columns[49],
        data.columns[50],
        data.columns[51]]

class Placeholder:
    def __init__(self, mydb, nameToInsert, nameToDelete):
        if (mydb.is_connected()): # if connected to a database, initialize variables
            self.mycursor = mydb.cursor() # mydb has to be defined first
            self.mydb = mydb
            self.nameToInsert = nameToInsert
            self.nameToDelete = nameToDelete
        else:
            raise Exception ("Database is not connected")   

    def deleteData(self,rango, name, nameToDelete): # Deletes data in a range
        mycursor = self.mycursor
        mydb = self.mydb
        for i in range(rango[0],rango[1] + 1):
            mycursor.execute(f"DELETE FROM excelnellie.{nameToDelete} WHERE {nameToDelete}_id= {i};")
            mydb.commit()

    def deleteDataSpec(self, name, nameToDelete, lenght, x): # Deletes specific data
        mycursor = self.mycursor
        mydb = self.mydb
        for i in range(0,lenght):
            mycursor.execute(f"DELETE FROM excelnellie.{nameToDelete} WHERE {nameToDelete}_id= {x[i]};")
            mydb.commit()

    def fetchAll(self): # Print database
        mycursor = self.mycursor
        mydb = self.mydb
        mycursor.execute(f"SELECT * FROM excelnellie.test2;")
        myresult = mycursor.fetchall()
        mydb.commit()
        print(myresult[5])
        # for x in myresult:
        #     print(x)

    def createCSV(self): # List to CSV file
        mycursor = self.mycursor
        mydb = self.mydb
        mycursor.execute(f"SELECT * FROM excelnellie.test2 WHERE data_width = 128;")
        myresult = mycursor.fetchall()
        mydb.commit()
        df = pd.DataFrame(myresult)
        df.to_csv('test1.csv', index = False, header=headerList)


    def closeCursor(self):
        self.mycursor.close()

    def createTable (self, data, nameOfTable): # Creates tables inside the database
        mycursor = self.mycursor
        mydb = self.mydb

        mycursor.execute(f"""CREATE TABLE {nameOfTable} (
        {nameOfTable}_id integer primary key AUTO_INCREMENT,
        {data.columns[0]} text,
        {data.columns[1]} text,
        {data.columns[2]} text,
        {data.columns[3]} text,
        {data.columns[4]} text,
        {data.columns[5]} text,
        {data.columns[6]} text,
        {data.columns[7]} text,
        {data.columns[8]} text,
        {data.columns[9]} text,
        {data.columns[10]} text,
        {data.columns[11]} text,
        {data.columns[12]} text,
        {data.columns[13]} text,
        {data.columns[14]} text,
        {data.columns[15]} text,
        {data.columns[16]} text,
        {data.columns[17]} text,
        {data.columns[18]} text,
        {data.columns[19]} text,
        {data.columns[20]} text,
        {data.columns[21]} text,
        {data.columns[22]} text,
        {data.columns[23]} text,
        {data.columns[24]} text,
        {data.columns[25]} text,
        {data.columns[26]} text,
        {data.columns[27]} text,
        {data.columns[28]} text,
        {data.columns[29]} text,
        {data.columns[30]} text,
        {data.columns[31]} text,
        {data.columns[32]} text,
        {data.columns[33]} text,
        {data.columns[34]} text,
        {data.columns[35]} text,
        {data.columns[36]} text,
        {data.columns[37]} text,
        {data.columns[38]} text,
        {data.columns[39]} text,
        {data.columns[40]} text,
        {data.columns[41]} text,
        {data.columns[42]} text,
        {data.columns[43]} text,
        {data.columns[44]} text,
        {data.columns[45]} text,
        {data.columns[46]} text,
        {data.columns[47]} text,
        {data.columns[48]} text,
        {data.columns[49]} text,
        {data.columns[50]} text,
        {data.columns[51]} text
        );""")

        mydb.commit()

    def fullInsert(self, params, data, naneToInsert): # Insert function
        mycursor = self.mycursor
        mydb = self.mydb
        nameToInsert = self.nameToInsert

        mycursor.execute(f"""INSERT INTO excelnellie.{nameToInsert} (
        {data.columns[0]},
        {data.columns[1]},
        {data.columns[2]},
        {data.columns[3]},
        {data.columns[4]},
        {data.columns[5]},
        {data.columns[6]},
        {data.columns[7]},
        {data.columns[8]},
        {data.columns[9]},
        {data.columns[10]},
        {data.columns[11]},
        {data.columns[12]},
        {data.columns[13]},
        {data.columns[14]},
        {data.columns[15]},
        {data.columns[16]},
        {data.columns[17]},
        {data.columns[18]},
        {data.columns[19]},
        {data.columns[20]},
        {data.columns[21]},
        {data.columns[22]},
        {data.columns[23]},
        {data.columns[24]},
        {data.columns[25]},
        {data.columns[26]},
        {data.columns[27]},
        {data.columns[28]},
        {data.columns[29]},
        {data.columns[30]},
        {data.columns[31]},
        {data.columns[32]},
        {data.columns[33]},
        {data.columns[34]},
        {data.columns[35]},
        {data.columns[36]},
        {data.columns[37]},
        {data.columns[38]},
        {data.columns[39]},
        {data.columns[40]},
        {data.columns[41]},
        {data.columns[42]},
        {data.columns[43]},
        {data.columns[44]},
        {data.columns[45]},
        {data.columns[46]},
        {data.columns[47]},
        {data.columns[48]},
        {data.columns[49]},
        {data.columns[50]},
        {data.columns[51]})
        values ( '{params[0]}',
        '{params[1]}',
        '{params[2]}',
        '{params[3]}',
        '{params[4]}',
        '{params[5]}',
        '{params[6]}',
        '{params[7]}',
        '{params[8]}',
        '{params[9]}',
        '{params[10]}',
        '{params[11]}',
        '{params[12]}',
        '{params[13]}',
        '{params[14]}',
        '{params[15]}',
        '{params[16]}',
        '{params[17]}',
        '{params[18]}',
        '{params[19]}',
        '{params[20]}',
        '{params[21]}',
        '{params[22]}',
        '{params[23]}',
        '{params[24]}',
        '{params[25]}',
        '{params[26]}',
        '{params[27]}',
        '{params[28]}',
        '{params[29]}',
        '{params[30]}',
        '{params[31]}',
        '{params[32]}',
        '{params[33]}',
        '{params[34]}',
        '{params[35]}',
        '{params[36]}',
        '{params[37]}',
        '{params[38]}',
        '{params[39]}',
        '{params[40]}',
        '{params[41]}',
        '{params[42]}',
        '{params[43]}',
        '{params[44]}',
        '{params[45]}',
        '{params[46]}',
        '{params[47]}',
        '{params[48]}',
        '{params[49]}',
        '{params[50]}',
        '{params[51]}'
        );""")

        mydb.commit()

        
class Prompts:
    def __init__(self):
        pass

    def menu(self):
        return ("1. Create table\n2. Insert data\n3. Delete data\n4. Custom query\n5. Exit\n6. Preview data\n7. Generate CSv")

    def successful(self):
        return ("------Database modified correctly------\n")

    def WelcomeMessage(self):
        return ("Welcome to the database management tool, currently you connection is")

    def switchStatement(self, UserInput):
        switcher = {
            1: print (1),
            2: print (2),
            3: print (3),
            4: print (4),
            5: print (5),
        } 
        return switcher.get(UserInput, "Invalid input")

