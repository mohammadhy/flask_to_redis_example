#--------------------------------------
from redis import Redis
from time import sleep
#---------------------------------------
redis = Redis(decode_responses=True)
print(redis.ping())
#---------------------------------------
pipeline = redis.pipeline()
pipeline.watch("test1", "test2")
sleep(5)
test1 = redis.get("test1")
test2 = redis.get("test2")

pipeline.multi()
pipeline.set("test1", test1 + " " + test2)
pipeline.execute()

