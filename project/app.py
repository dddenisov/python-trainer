from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/ping")
def pong():
    return "Pong"

@app.route("/post", methods=['POST'])
def post_method():
    text = request.form["data"]
    return text

if __name__ == '__main__':
    app.run()
