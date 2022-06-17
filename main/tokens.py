import datetime
import pytz
import jwt
from jwt.exceptions import ExpiredSignatureError

SECRET_KEY = "9fba12bc2a8d69d57217ee0d1692123f0c9ff06a365b51e627acdc596e1e3826d57d934c01374f6bb34d48900d04a4c1f51b8577499a5295ef3cf1ff3d838dee"  # paste secret key here | run openssl rand -hex 64
ALGORITHM = "HS256"
TOKEN_EXPIRE = 60 * 24  # one day


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
