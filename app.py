from flask import Flask, render_template
from modules.grabber import get_weather

import os

try:
    APP_ID = os.environ['APP_ID']
    print(APP_ID)
except KeyError:
    print('Please set APP ID key as environment variable.')
    raise

app = Flask(__name__)

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(
        dict(
            # Default is '{{', I change this because Vue.js uses '{{' / '}}'
            variable_start_string='%%',
            variable_end_string='%%',
        ))

app = CustomFlask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_weather/<string:city>')
def predict_weather(city):
    return str(get_weather(city, APP_ID))

if __name__ == '__main__':
    print('app {} run'.format(__name__))
    app.run(debug=True, port=8000, host='0.0.0.0')
