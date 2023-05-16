from flask import Flask
from redis import Redis



app = Flask(__name__)

redis = Redis(decode_responses=True)
## getset: show current stat and set new key value
old = redis.getset("counter", "1")

print(old)
@app.route("/")
def index():
    redis.incr("counter")
    return "My Flask App"

@app.route("/stat")
def stats():
    counter = redis.get("counter")
    return f"current counter is {counter} and Last server-counter before restart was {old}"


if __name__ == "__main__":
    app.run(host="192.168.42.144")

