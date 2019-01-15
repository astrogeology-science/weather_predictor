import requests

def get_weather(city, app_id):
    request_string = \
        'http://api.openweathermap.org/data/2.5/weather?q='+\
        city+'&appid='+app_id

    r = requests.get(request_string)
    if r.ok:
        print(r.json())
        return r.json()
    else:
        return r.status_code
