import json
import pandas as pd
from Data import GetData

class DataElaboration():
    json = str()
    
    def __init__(self, json):
        self.json = json
    
    def Elaborate(self):
        df = pd.read_json(json.dumps(self.json), typ='series')
        return print(df)

data = GetData()
data.GetFromAccountTable()
d = DataElaboration(data.jd)
d.Elaborate()