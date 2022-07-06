import json
import datetime
import pandas as pd
import azure.functions as func
from modules import Data, NightElaboration

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()