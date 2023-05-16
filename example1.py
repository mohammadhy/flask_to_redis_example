from redis import Redis

redis = Redis(decode_responses=True)
### check Establishe conntection
#print(redis.ping())



if redis.ping() is True:
    print("Conntected To Redis Successfully")
    print(redis.get("name"))
    print(redis.get("login"))
    print(redis.hgetall(redis.get("login")))
    info = redis.hgetall("username:1")
    print(info["name"])
else:
    print("Not Available Server")




contries = [
        { "id": "345654535416545",
          "name": "Iran"
        },

        { "id": "545454844464",
          "name": "London"
        }

]

for contrie in contries:
    redis.hset (
            ":".join(["contries", contrie.get("id")]),
            mapping = contrie
            )



if redis.ping is True:
    print(redis.hgetall(redis.get("login")))
