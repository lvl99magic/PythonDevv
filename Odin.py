from sqlalchemy import create_engine
import pyodbc

server = 'WSAMZN-IBOS3L3K\MSSQLSERVER10'
db = 'AdventureWorks2019'
driver = 'SQL Server Native Client RDA 11.0'

sqlcon = create_engine('mssql+pyodbc://@' + server + '/' + db + '?trusted_connection=yes&driver=' + driver + '')
