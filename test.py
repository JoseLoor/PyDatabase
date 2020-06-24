import os

import mysql.connector
import pandas as pd
from dotenv import load_dotenv
from mysql.connector import errorcode

import functions as func

load_dotenv()

# DELETE FROM excelnellie.test5 WHERE test5_id= 30;

data = pd.read_csv("test_dataset_for_yahia.csv") # CSV where we are getting the data

exitStatement = True

mydb = mysql.connector.connect(host=os.getenv("DB_HOST"),   # Connect to the database
                                user=os.getenv("DB_USER"),   
                                passwd=os.getenv("DB_PASSWORD"),
                                database = os.getenv("DB_DATABASE"),
                                auth_plugin=os.getenv("DB_AUTHPLUGIN"))  

counter = 1
wait = ""

testString = "works"

Prompts = func.Prompts() # Creates object Prompts
Hola = func.Placeholder(mydb, wait, wait) # Creates object Hola

print(Prompts.WelcomeMessage() + " " + str(mydb.is_connected()))

while exitStatement:
    UserInput = input (Prompts.menu() + "\n")
    if UserInput == '1':
        nameOfTable = input ("Name of new table: ")
        Hola.createTable(data, nameOfTable)
        print(Prompts.successful())

    elif UserInput == '2':
        nameToInsert = input ("In which table do you want to insert the data?\n")
        numberToInsert = input ("How many rows?\n")
        InsertFuncs = func.Placeholder(mydb, nameToInsert, wait) # Initilize object to insert funcs
        for row in range(int(numberToInsert)): # Iterates through csv file
            params = []
            for columns in data.columns:
                params.append(data[columns][row])
            InsertFuncs.fullInsert(params, data, nameToInsert) # Function to insert data 
            print("row " + str(row + 1) + " inserted")    
        print("\n")
        print(Prompts.successful())

    elif UserInput == '3':
        nameToDelete = input ("In which table do you want to delete data?\n")
        UserInputDel = input("1. Delete in a range\n2. Delete specific rows\n")
        DeleteFuncs = func.Placeholder(mydb, nameToDelete, wait) # Initilize object to delete funcs
        if UserInputDel == '1':
            rangeDel1 = input ("Please input the first number for the range: ")
            rangeDel2 = input ("Please input the second number for the range: ")
            rango = [int(rangeDel1), int(rangeDel2)]
            DeleteFuncs.deleteData(rango, wait, nameToDelete)
            print("\n")
            print(Prompts.successful())
        elif UserInputDel == '2':
            x = list(map(int, input("Please enter the rows that want to be deleted: ").split())) 
            lenght = len(x)
            DeleteFuncs.deleteDataSpec(wait, nameToDelete, lenght, x)
            print("\n")
            print(Prompts.successful())

    elif UserInput == '4':
        query = input ("Please input query: \n")
        mycursor = mydb.cursor()
        try:
            mycursor.execute(query)
            mydb.commit()
            print("\n")
            print(Prompts.successful())
        except:
            print("\n------Error in the query, Please try again------\n")

    elif UserInput == '5':
        Hola.closeCursor()
        mydb.close()
        exitStatement = False

    else:
        print ("Invalid input")