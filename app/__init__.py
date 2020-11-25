import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return { 'hello': ["w", "o", "r", "l", "d"]}