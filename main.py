from flask import Flask
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas

app = Flask(__name__)


def predict():
    path = 'https://raw.githubusercontent.com/speianudana/FIA/main/Lab3/apartmentComplexData.txt'
    columns = ['1', '2', 'complex_age', 'total_rooms', 'total_bedrooms', 'complex_inhabitants', 'apartments_nr', '8',
               'median_complex_value']

    dataset = pandas.read_csv(path, names=columns)
    dataset.describe()

    dataset.corr()
    x = dataset[
        ['1', '2', 'complex_age', 'total_rooms', 'total_bedrooms', 'complex_inhabitants', 'apartments_nr', '8']]

    y = dataset[['median_complex_value']].values.flatten()

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=70)

    training = LinearRegression().fit(x_train, y_train)
    training_score = training.score(x_train, y_train)
    testing_score = training.score(x_test, y_test)
    actual_price = y_test[0]
    predicted_price = training.predict([x_test.iloc[0]])[0]

    return training_score, testing_score, actual_price, predicted_price


@app.route("/")
def index():
    prediction = predict()[0]
    return "Prediction: {}" + format(prediction)


# @app.route('/predict')
# def hello_name():
#     return predict()[0]


if __name__ == '__main__':
    app.run()
