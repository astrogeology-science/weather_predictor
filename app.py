from flask import Flask, render_template
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
    return city

if __name__ == '__main__':
    print('app {} run'.format(__name__))
    app.run(debug=True, port=8000, host='0.0.0.0')
