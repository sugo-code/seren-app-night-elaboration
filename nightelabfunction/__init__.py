import json
import datetime
import azure.functions as func
from modules import DataElaboration

data = DataElaboration()

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    data.CalculateMedians()