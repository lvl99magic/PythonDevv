import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server Native Client RDA 11.0};"
                      "Server=WSAMZN-IBOS3L3K\MSSQLSERVER10;"
                      "Database=AdventureWorks2019;"
                      "Trusted_Connection=yes;")