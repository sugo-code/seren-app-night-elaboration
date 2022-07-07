import json
import warnings
from decouple import config
from datetime import datetime, timedelta
from azure.data.tables import TableClient
from azure.core.exceptions import HttpResponseError

warnings.filterwarnings('ignore')

class GetData():
    cs = config("CONNECTION_STRING")
    table = config("TABLE")
    jd = list()
    count = 0
    
    def Get(self):
        with TableClient.from_connection_string(conn_str=self.cs, table_name=self.table) as client:
            try:
                dt = str(datetime.today() - timedelta(days=1)).replace(" ", "T")
                # parameters = {"datetime": dt}
                parameters = {"btryLvl": 100}
                query_filter = "Battery le @btryLvl"
                queried_entities = client.query_entities(query_filter=query_filter,parameters=parameters)
                for e in queried_entities:
                    self.jd.append(e)
                return self.jd
                self.jd.clear()
            except HttpResponseError as err:
                return(err)
    
# data = GetData()
# print(data.Get())