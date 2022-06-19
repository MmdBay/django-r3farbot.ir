from persiantools.jdatetime import JalaliDateTime, timedelta
import requests
import pytz
from config import core


def create_payment(order_id: str, amount: int, callback: str):
    try:
        headers = {"Content-Type": "application/json", "X-API-KEY": core.Main.API_KEY,
                   "X-SANDBOX": "0"}  # change X-SANDBOX to 0, 1 is for test
        data = {"order_id": order_id, "amount": amount, "callback": callback}
        response = requests.post(url="https://api.idpay.ir/v1.1/payment", json=data, headers=headers, timeout=60)
        if response.status_code == 201:
            return response.json()
    except requests.RequestException:
        return False


def verify_payment(idpay_id: str, order_id: str):
    try:
        headers = {"Content-Type": "application/json", "X-API-KEY": core.Main.API_KEY,
                   "X-SANDBOX": "0"}
        data = {"order_id": order_id, "id": idpay_id}
        response = requests.post(url="https://api.idpay.ir/v1.1/payment/verify", json=data, headers=headers, timeout=60)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        return False


def activate_time(days) -> str:
    expire_date = JalaliDateTime.strptime(get_now(), "%Y:%m:%d %H-%M-%S") + timedelta(days=days)
    expire_date = expire_date.strftime("%Y:%m:%d %H-%M-%S")
    return expire_date


def find_plan(amount: int) -> list:
    amount_lists = [[80000, 160000], [100000, 200000], [120000, 240000]]
    plan_time = [31, 61]
    plan_type = ['bronze', 'silver', 'gold']

    for index, value in enumerate(amount_lists):
        for index1, value1 in enumerate(value):
            if amount == value1:
                return [plan_type[index], plan_time[index1]]


def timestamp_to_time(timestamp: int) -> str:
    return str(JalaliDateTime.fromtimestamp(timestamp))


def get_now() -> str:
    date = JalaliDateTime.now(tz=pytz.timezone("Asia/Tehran"))
    date = date.strftime("%Y:%m:%d %H-%M-%S")
    return date
