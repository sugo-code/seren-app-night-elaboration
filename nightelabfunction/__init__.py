import json
import datetime
import pandas as pd
from modules import data
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    Elaborate(data.GetData())
    
def Elaborate(jsondata: dict()):
    df = pd.read_json(jsondata)
    return df