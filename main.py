from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template('index.html', year=current_year)




@app.route('/<name>')
def make_guess(name):
    params = {
        "name": f"{name}"
    }

    response_gender = requests.get(url="https://api.genderize.io", params=params)
    response_age = requests.get(url="https://api.agify.io", params=params)
    your_name = name
    your_gender = response_gender.json()["gender"]
    your_age = response_age.json()["age"]

    return render_template('guess.html', name=your_name, gender=your_gender, age=your_age)

if __name__ == "__main__":
    app.run(debug=True)



