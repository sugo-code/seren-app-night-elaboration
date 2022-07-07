import sys
import datetime
import azure.functions as func
sys.path.insert(1, r'C:\Users\Devis\Desktop\Project Work anno 2\Function - Night Elaboration\NightElab\modules')

from elaboration import UploadData

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    UploadData()
