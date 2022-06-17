from persiantools.jdatetime import JalaliDateTime
import multiprocessing
import requests
import pytz
import math

bot_token = ""


def get_users(_queue: multiprocessing.Queue):
    try:
        response = requests.get(
            f"https://api.telegram.org/bot{bot_token}/"
            "getChatMemberCount?chat_id=@r3farbot",
            timeout=4
        )
        _queue.put(response.json()['result'] if response.status_code == 200 else 0)
    except requests.ConnectTimeout:
        return 0


def get_name(chat_id: int):
    response = requests.get(
        f"https://api.telegram.org/bot{bot_token}/"
        f"getChat?chat_id={chat_id}"
    )
    return response.json()['result'] if response.status_code == 200 else False


def get_now():
    date = JalaliDateTime.now(tz=pytz.timezone("Asia/Tehran"))
    date = date.strftime("%Y/%m/%d %H:%M:%S")
    return date


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 بایت"
    size_name = ("بایت", "کیلوبایت", "مگابایت", "گیگابایت", "Tb", "Pb", "Eb", "Zb", "Yb")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


class SizeCalculator:

    def __init__(self, plan, download_usage):
        self.plan = plan
        self.download_usage = download_usage

        self.free = 1610000000
        self.bronze = 16106127360
        self.silver = 26843545600
        self.gold = 37580963840

    def get_remain_usage(self):

        if self.plan == 'free':
            return self.free - int(self.download_usage)
        elif self.plan == 'bronze':
            return self.bronze - int(self.download_usage)
        elif self.plan == 'silver':
            return self.silver - int(self.download_usage)
        elif self.plan == 'gold':
            return self.gold - int(self.download_usage)


class PremiumUserClass:

    def __init__(self,
                 premium,
                 private_key,
                 user,
                 usage_y,
                 downloads_y,
                 buy_counts,
                 is_connected,
                 downloads_i,
                 usage_u,
                 downloads_u
                 ):

        self.premium = premium
        self.private_key = private_key
        self.user = user
        self.usage_y = usage_y
        self.downloads_Y = downloads_y
        self.buy_counts = buy_counts
        self.is_connected = is_connected
        self.downloads_i = downloads_i
        self.usage_u = usage_u
        self.downloads_u = downloads_u

        self.name = None
        self.chat_id = None
        self.email = None
        self.user_private_key = None
        self.plan_type = None
        self.buy_date = None
        self.expire_date = None
        self.status = None

        self.down_usage_y = None
        self.remain_usage_y = None

        self.down_usage_u = None
        self.remain_usage_u = None

    def get_into(self):

        self.chat_id = self.premium.chat_id if self.premium else self.private_key.chat_id if self.private_key else 0
        self.name = get_name(self.premium.chat_id)['first_name'] if self.premium else \
            get_name(self.private_key.chat_id)['first_name']
        self.email = self.user.email if self.user else 'user@user.com'
        self.user_private_key = self.user.private_key[0:10]
        self.plan_type = self.premium.plan_type if self.premium else 'free'
        self.buy_date = self.premium.buy_date if self.premium else '00-00-00 00:00:00'
        self.expire_date = self.premium.expire_date if self.premium else '00-00-00 00:00:00'
        self.status = self.premium.status if self.premium else 'Active'

        self.down_usage_y = convert_size(int(self.usage_y.usage_du)) if self.usage_y is not None else convert_size(0)
        self.remain_usage_y = convert_size(
            SizeCalculator(self.plan_type, self.usage_y.usage_du if self.usage_y is not None else 0).get_remain_usage())

        self.is_connected = "متصل" if self.is_connected else "نامعلوم"
        self.downloads_i = self.downloads_i

        self.down_usage_u = convert_size(int(self.usage_u.usage_do)) if self.usage_u is not None else convert_size(0)
        self.remain_usage_u = convert_size(
            SizeCalculator(self.plan_type, self.usage_u.usage_do if self.usage_u is not None else 0).get_remain_usage())

