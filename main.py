import psutil
import os
import requests
from dotenv import load_dotenv
from typing import Union, Any


load_dotenv()
API_URL = os.getenv('API_URL')
MEMORY_LIMIT = float(os.getenv('MEMORY_LIMIT'))


def convert_to_mb(memory_value: int) -> float:
    return memory_value / 1000000


def get_used_ram() -> Union[Any, float]:
    memory_info = psutil.virtual_memory()
    percentage_usage, mb_usage = memory_info[2], memory_info[3]
    return percentage_usage, convert_to_mb(mb_usage)


def send_alarm() -> bool:
    request = requests.post(API_URL)
    if request.status_code == 200:
        return True
    else:
        return False


while True:
    memory_used_percents, memory_used_value = get_used_ram()
    if memory_used_value > MEMORY_LIMIT:
        alarm_status = send_alarm()
        if alarm_status:
            print("Alarm successfully sent")
        else:
            print("Alarm didn't send")