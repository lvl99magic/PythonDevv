import pandas as pd
import datacompy
from Odin import sqlcon

# unrealistic comparisons
# class quiteIntheLibrary():
#     def proggress(self, tblName, sqlCnxn, shcma):
#         pd.read_sql_table()
#
# data1 = pd.read_sql_table("BusinessEntityAddress", sqlcon, schema='carson')
# data2 = pd.read_sql_table("Address", sqlcon, schema='carson')


class compObject:
    def __init__(self, t1, t2, s1, s2, r):
        self.tbl1 = t1
        self.tbl2 = t2
        self.schema1 = s1
        self.schema2 = s2
        self.compReport = r


def compReport(tbl1, tbl2, schema1, schema2, jC='rowguid'):

    data3 = pd.read_sql_table(tbl1, sqlcon, schema=schema1)
    data4 = pd.read_sql_table(tbl2, sqlcon, schema=schema2)
    # compare function params
    df1Name = schema1 + '.' + tbl1
    df2Name = schema2 + '.' + tbl2
    compare0 = datacompy.Compare(
        data3,
        data4,
        join_columns=jC,  #You can also specify a list of columns
        abs_tol=0, #Optional, defaults to 0
        rel_tol=0, #Optional, defaults to 0
        df1_name=df1Name, #Optional, defaults to 'df1'
        df2_name=df2Name #Optional, defaults to 'df2'
        )
    compare0.matches(ignore_extra_columns=False)
    cReport = compare0.report()
    compObj = compObject(tbl1, tbl2, schema1, schema2, cReport)
    return compObj
