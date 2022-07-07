import json
import warnings
import pandas as pd
import urllib.parse
from .data import GetData
from decouple import config
from sqlalchemy import create_engine
from datetime import datetime, timedelta
warnings.filterwarnings('ignore')

# Environment Variables
server = config("SERVER")
database = config("DATABASE") 
username = "itsuser"
password = config("PASSWORD")
driver = config("DRIVER")

# Create DB Connection with SQLAlchemy
odbc_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+username+';DATABASE='+ database + ';PWD='+ password
connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote(odbc_str)
engine = create_engine(connect_str)

class DataElaboration():
    json = str()
    
    def __init__(self):
        self.json = self.GetData()
        self.data = self.CreateDataframe()
        self.bodytmp = self.CalculateBodyTemperatureMean()
        self.bldprs = self.CalculateBloodPressureMean()
        self.bldoxg = self.CalculateBloodOxygenMean()
        self.btr = self.CalculateBatteryMean()
        self.hrtfrq = self.CalculateHeartFrequencyMean()
        
    def GetData(self):
        d = GetData()
        return json.dumps(d.Get())
    
    def CreateObject(self):
        obj = dict()
        obj.update({'BodyTemperature': self.bodytmp, 'BloodPressure': self.bldprs, 'BloodOxygen': self.bldoxg, 'Battery': self.btr, 'HeartFrequency': self.hrtfrq})
        return obj
    
    def CreateDataframe(self):
        df = pd.read_json(self.json)
        return df
    
    def CalculateBodyTemperatureMean(self):
        df = self.data
        df[df['RowKey']>=str((datetime.now() - timedelta(days=1)))]['BodyTemperature']
        df = df[['BodyTemperature']].mean()
        data = json.loads(df.to_json())
        return data['BodyTemperature']
    
    def CalculateBloodPressureMean(self):
        df = self.data
        df[df['RowKey']>=str((datetime.now() - timedelta(days=1)))]['BloodPressure']
        df = df[['BloodPressure']].mean()
        data = json.loads(df.to_json())
        return data['BloodPressure']
    
    def CalculateBloodOxygenMean(self):
        df = self.data
        df[df['RowKey']>=str((datetime.now() - timedelta(days=1)))]['BloodOxygen']
        df = df[['BloodOxygen']].mean()
        data = json.loads(df.to_json())
        return data['BloodOxygen']
    
    def CalculateBatteryMean(self):
        df = self.data
        df[df['RowKey']>=str((datetime.now() - timedelta(days=1)))]['Battery']
        df = df[['Battery']].mean()
        data = json.loads(df.to_json())
        return data['Battery']
    
    def CalculateHeartFrequencyMean(self):
        df = self.data
        df[df['RowKey']>=str((datetime.now() - timedelta(days=1)))]['HeartFrequency']
        df = df[['HeartFrequency']].mean()
        data = json.loads(df.to_json())
        return data['HeartFrequency']
    
def UploadData():
    d = DataElaboration()
    jdata = d.CreateObject()
    try:
        engine.execute(f"INSERT INTO dbo.DeviceReports(ID, BodyTemperatureAvg, BloodPressureAvg, BloodOxygenAvg, BatteryAvg, HeartFrequencyAvg) VALUES (\'{datetime.now() - timedelta(days=1)}\', {float(jdata['BodyTemperature'])}, {float(jdata['BloodPressure'])}, {float(jdata['BloodOxygen'])}, {float(jdata['Battery'])}, {int(jdata['HeartFrequency'])})")
        return f"{datetime.now()}: Data correctly inserted!"
    except:
        return f"{datetime.now()}: Something wrong, data not inserted..."