from flask import session
from models import storage, User


def user_profile():
    res = {}

    handle = session.get("handle")
    if handle is None:
        return None

    user = storage.getDict(User, {'handle':handle})

    if not user:
        return None
    user = user[0]

    # add number of solved problems.
    solved = 0

    res = {
        'handle':user.handle,
        'rate': user.rate,
        'status': user.status,
        'solved': solved,
        'age': user.age,
        'gender':user.gender
    }

    return res
