import json
import warnings
from decouple import config
from datetime import datetime, timedelta
from azure.data.tables import TableClient
warnings.filterwarnings('ignore')

class GetData():
    cs = config("CONNECTION_STRING")
    table = config("TABLE")
    
    def Get(self):
        client = TableClient.from_connection_string(conn_str=self.cs, table_name=self.table)
        dt = str(datetime.today() - timedelta(days=1)).replace(" ", "T")
        parameters = {"datetime": dt}
        query_filter = "Battery le 100"
        table = client.query_entities(query_filter=query_filter, parameters=parameters)
        for e in table:
            for k in e.keys():
                return json.dumps(f"Key: {k}, Value: {e[k]}")    