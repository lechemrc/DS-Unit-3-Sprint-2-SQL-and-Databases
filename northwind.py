import sqlite3
# UNCOMMENT AND USE CODE BELOW IF northwind_small.sqlite3 FILE NOT IN LOCAL STORAGE
# !wget https://github.com/lechemrc/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/\
#               northwind_small.sqlite3?raw=true -O northwind_small.sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Viewing table names
curs.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    )
result = curs.fetchall()
print(f'The table names are: \n{result}\n')

# Ten most expensive products
curs.execute("""
    SELECT ProductName, UnitPrice 
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
""")
result = curs.fetchall()
print(f'The ten most expensive items are: \n{result}\n')

# Average age at hiring date
curs.execute("""
    SELECT SUM(HireDate - BirthDate) / COUNT(*)
    FROM Employee
""")
result = curs.fetchall()
print(f'The average age at hiring is {result}.\n')

# STRETCH GOAL

# Average age of hiring date grouped by city
curs.execute("""
    SELECT City, SUM(HireDate - BirthDate) / COUNT(*)
    FROM Employee
    GROUP BY City
""")
result = curs.fetchall()
print(f'The average age at hiring based on city is: \n{result}.\n')

# SC Part 3

# To check table column names
curs.execute(
    'PRAGMA table_info(Product);'
).fetchall()

# To check table column names
curs.execute(
    'PRAGMA table_info(Supplier);'
).fetchall()

# Ten most expensive products and their suppliers
curs.execute("""
    SELECT ProductName, UnitPrice, CompanyName
    FROM Product p
    LEFT JOIN Supplier s
    ON p.ID = s.ID
    ORDER BY UnitPrice DESC
    LIMIT 10
""")
result = curs.fetchall()
print(f'The ten most expensive products and their suppliers are: \n{result}\n')

# To check table column names
curs.execute(
    'PRAGMA table_info(Category);'
).fetchall()

# Largest category by number of unique products in it.
curs.execute("""
    SELECT CategoryName, COUNT(*) - COUNT(DISTINCT CategoryName) 
    FROM Product p
    LEFT JOIN Category c
    ON p.ID = c.ID
    ORDER BY CategoryName DESC
""")
result = curs.fetchall()
print(f'The largest category based on unique products is {result}\n')
# I did this query because by in large, most had the category of 'None' and count
# won't accept that unless I count all the CategoryNames then subtract the unique
# ones (i.e. non-null values), meaning that 69 had no category name.

# STRETCH GOAL
# Employee with most territories
curs.execute("""
    SELECT TerritoryID, COUNT(*) count
    FROM EmployeeTerritory et
    LEFT JOIN Employee e
    ON employeeID = e.ID
    GROUP BY EmployeeID
    ORDER BY count DESC
    LIMIT 1;
""")
result = curs.fetchall()
print(f'The employee with the most territories is {result}')

# Closing connection and committing
curs.close()
conn.commit()