from flask import Flask
from prediction import predict
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Training score: </h1>"


if __name__ == '__main__':
    app.run()
