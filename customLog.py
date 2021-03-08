from Stellar import cnxn
from datetime import datetime

class customLogger:
    def logInfo(self, status, scriptName):
        step = "INFO"
        self.__insertlog(step, status, scriptName)

    def logError(self, status, scriptName):
        step = "ERROR"
        self.__insertlog(step, status, scriptName)

    def __insertlog(self, step, status, scriptName):

        # step = a step in the function
        # status = idk
        # starttime = time at which the script made activity
        # script name = obvious

        now = datetime.now()
        startTime = now.strftime("%Y-%m-%d %H:%M:%S")
        cursor = cnxn.cursor()
        insertsql = "INSERT INTO [carson].[logs]\
                ([Step]\
               ,[Status]\
               ,[StartTime]\
               ,[ScriptName])\
         VALUES('{}', '{}', '{}', '{}')".format(step, status, startTime, scriptName)
        cursor.execute(insertsql)
        cursor.commit()
        #print(insertsql)