from flask import Flask, render_template, request
import requests
import pprint

app = Flask(__name__)

pp = pprint.PrettyPrinter(indent=4)
weather_url = "http://api.openweathermap.org/data/2.5/weather?"


@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/weather")
# def display_weather():
#     return render_template("index.html")

@app.route('/weather_results', methods=['GET', 'POST'])
def weather_results_page():
    city = request.args.get('city')
    
    params = {
        'q': city,
        'APPID': "3ec502b7313be393c9317bda5ae20cc4"
        }


    r = requests.get(weather_url, params=params)

    results = r.json()
    tempK = results['main']['temp']
    temp = kelvin_to_farenheit(tempK)

    print(results)


    return render_template('weather_results.html', results=results, temp=temp)

def kelvin_to_farenheit(k):
    results = 1.8 * (k-273) + 32
    return int(results)

if __name__ == '__main__':
    app.run()

