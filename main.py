from flask import Flask
from prediction import predict

app = Flask(__name__)


@app.route("/")
def index():
    prediction = predict()[0]
    return "Prediction: {}"+format(prediction)


# @app.route('/predict')
# def hello_name():
#     return predict()[0]


if __name__ == '__main__':
    app.run()
