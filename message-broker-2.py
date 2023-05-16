from json import loads
from redis import Redis
from base64 import b64decode
from time import sleep
redis = Redis(db=1,decode_responses=True)

pubsub = redis.pubsub()

pubsub.subscribe("new_user")

for message in pubsub.listen():
    print(message)
    if message["type"] == "message":
        user = loads(b64decode(message["data"]).decode('utf8'))
        sleep(5)
        print(user)
    else:
        print("..........")
