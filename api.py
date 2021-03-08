import json
import requests
import urllib.parse
import pandas as pd
from Odin import sqlcon
import csv
import customLog

customLog = customLog.customLogger()

def urlStorage(qry, limit):
    try:
        api_url_base = 'https://data.cms.gov/provider-data/api/1/datastore/sql?query='
        actualURL = api_url_base + urllib.parse.quote(qry + limit)
        # print(actualURL)
        header = {'Content-Type': 'application/json'}
        response = requests.get( 
        customLog.logInfo("The Api request was successfull!", __file__)
        return response
    except:
        customLog.logError("Could not make the API request.", __file__)

#       api data to json "Body" where .text = body
try: 
    x = str(urlStorage('[SELECT * FROM 5ec91940-5026-55ab-8f87-f2d308368b56]','[LIMIT 10 OFFSET 60]').text)
    j = json.loads(x)
    df = pd.DataFrame(j)
    customLog.logInfo("The API requests JSON body was converted", __file__)
except:
    customLog.logError("Could not convert the JSON body to a DataFrame", __file__)

try:
    df.to_sql('[wtf]', sqlcon, index=False, if_exists="append", schema="carson")
    customLog.logInfo("The DataFrame was injected into the DataBase!", __file__)
except:
    customLog.logError("The DataFrame was not injected to the DataBase", __file__)

# print(df)

# for emp in json.loads(str(x)):
#     print(emp['lst_nm'])

