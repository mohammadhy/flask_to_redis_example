from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(decode_responses = True)



@app.route("/login/<username>")
def login(username):
    redis.setex("login", "60", username)
    return f"Login {username}"


@app.route("/")
def index():
    if redis.exists("login"):
        redis.expire("login", 60)
        info = redis.hgetall(redis.get("login"))
        return info["name"]
    else:
        return "Somthing happeng Login Again.."
if __name__ == "__main__":
    app.run(host="192.168.42.144")
