# SQL guide

This is going to be a short guide on how to use some of SQL basic functions and get you computer set up to work with a database

## Installation

Because working in a virtual environment is always good practice, we are going to create our own. First, install the Python extension

```bash
pip install virtualenv
```

Then, to create the virtual environment in your project you need to run:

```bash
virtualenv venv  
```

Finally, every time you are going to start working, the virtual environment needs to be initialized with the following command

```bash
.\venv\Scripts\activate
```

This project has a *requirement.txt* file to set up all the python extensions you need to run it. To install them, just run the command: 

```bash
pip install -r .\requirement.txt
```

## Connecting to the database

This project contains a file called *.env.sample* which is a template for creating environmental variables which will work as the credentials for the database. This file is personal and should not be uploaded to any repository. 

## Accesing data

In order to see a table, run the following command 

```sql
SELECT * FROM table_name;
```

If you want to see only specific data, or sort it in a particular way, writing functions come in handy. Here are some examples:

```sql
-- How many different types of experiment are there
SELECT experiment, COUNT(experiment)
FROM excelnellie.test2 -- (table_name)
GROUP BY experiment;

-- How many different experiments per device
SELECT device, COUNT(device)
FROM excelnellie.test2 -- (table_name)
GROUP BY device;

-- Sort by data_width
SELECT*
FROM excelnellie.test2 -- (table_name)
ORDER BY data_width ASC;

-- Check is by having a data width of 128, we can achive fmax of more than 400
SELECT*
FROM excelnellie.test2 -- (table_name)
WHERE data_width = 128
HAVING fmax >= 400;

-- Sort ascending (what you new)
SELECT*
FROM excelnellie.test2 -- (table_name)
ORDER BY data_width ASC; -- Change data_width to whatever you are looking for

-- Sort descending (what you new)
SELECT*
FROM excelnellie.test2 -- (table_name)
ORDER BY data_width DESC; -- Change data_width to whatever you are looking for
```

Inserting data manually is also possible, although it is not recommend because it is a tedious process when you are working with large databases. In our case, to insert a full row of data, we would have to type all 52 fields. 

Sample code:

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

## Update/Delete data

In order to delete a whole entry, run the following line

```sql
DELETE FROM table_name WHERE condition;
```

Example:

```sql
DELETE FROM excelnellie.test2 WHERE test2_id= 21;
```

If we don't want to dete the whole row, but just update certain cells, the Update keyword is very useful. 

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

Example:

```sql
UPDATE excelnellie.test2
SET combo = 10, device = 50
WHERE test2_id=23;
```

## Storing data

Excel has a function to directly connect your csv files to MySQL. 

![image](https://user-images.githubusercontent.com/36271578/84598922-347b7b80-ae3c-11ea-89c4-61cee3ded686.png)

This is also possible using Python. The main two libraries that we use for this is Pandas to access the csv and mysqlconnector to connect to the database. 

First, we load the csv file:

```python
data = pd.read_csv("test_dataset_for_yahia.csv")
```

Then, establish the connection with the database:

```python
mydb = mysql.connector.connect(host=os.getenv("DB_HOST"),   
                                user=os.getenv("DB_USER"),   
                                passwd=os.getenv("DB_PASSWORD"),
                                 database = os.getenv("DB_DATABASE"),
                                auth_plugin=os.getenv("DB_AUTHPLUGIN")) 
```

