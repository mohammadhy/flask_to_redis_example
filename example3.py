from flask import Flask 
from redis import Redis




app = Flask(__name__)

redis = Redis(decode_responses = True)

@app.route("/login")
def login():
    redis.setex("login", "60", "expire_time")
    return "Successfully login ...."



@app.route("/")
def index():
    if redis.exists("login"):
        redis.expire("login", "60")
        return "Welcome To Flask App Microservice By noob.hy"
    else:
        return "Oops! \n Somethings Happen You Need To Login Again ...."

if __name__ == "__main__":
    app.run(host="192.168.42.144")
