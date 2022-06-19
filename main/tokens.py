import datetime
import pytz
import jwt
from jwt.exceptions import ExpiredSignatureError
from config import core

SECRET_KEY = core.Main.SECRET_KEY  # paste secret key here | run openssl rand -hex 64
ALGORITHM = "HS256"
TOKEN_EXPIRE = 60 * 60 * 24  # one day


def encode(data: dict):
    datas = data.copy()
    datas.update(
        {"exp": datetime.datetime.now(tz=pytz.timezone("Asia/Tehran")) + datetime.timedelta(minutes=TOKEN_EXPIRE)})

    token = jwt.encode(
        payload=datas,
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def decode(token):
    try:

        dce = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return dce

    except ExpiredSignatureError:
        return False
