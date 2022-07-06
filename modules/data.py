import json
import warnings
from decouple import config
from datetime import datetime, timedelta
from azure.data.tables import TableClient
warnings.filterwarnings('ignore')

class GetData():
    cs = config("CONNECTION_STRING")
    table = config("TABLE")
    jd = {}
    
    def GetFromAccountTable(self):
        try:
            client = TableClient.from_connection_string(conn_str=self.cs, table_name=self.table)
        except:
            return "No connection could be made"
        dt = str(datetime.today() - timedelta(days=1)).replace(" ", "T")
        parameters = {"datetime": dt}
        query_filter = "RowKey le @datetime"
        try:
            table = client.query_entities(query_filter=query_filter, parameters=parameters)
            for e in table:
                for k in e.keys():
                    self.jd.update({'Key': k, 'Value': e[k]})
            return self.jd
        except:
            return "Cannot query the database, no results found"