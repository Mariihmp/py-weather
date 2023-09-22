from flask import Flask, redirect, render_template, request, url_for
from weather import get_current_weather


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not bool(city.strip()):
        city = "London"
    weather_data = get_current_weather(city)
    if not weather_data['cod'] == 200:
        # return redirect(url_for('index'))
        return redirect(url_for('index'))
    return render_template('weather.html', title=weather_data['name'], status=weather_data['weather'][0]['description'].capitalize(),          temp=weather_data['main']['temp'], feels_like=weather_data['main']['feels_like']
                           )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
