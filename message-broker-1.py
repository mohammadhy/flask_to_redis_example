from base64 import b64encode
from json import dumps
from redis import Redis
from time import sleep
redis = Redis(db=1)

user = {
        "username": "noob",
        "password": "hy"
        }

if redis.ping is False:
    raise Exception("Stiil Not Connection Establishe")
else:
    print(redis.publish("new_user", b64encode(dumps(user).encode('ascii'))))

