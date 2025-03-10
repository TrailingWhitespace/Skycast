from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/weather", methods = ["POST"])
def weather():
    if request.method == "POST":
        with open("api_key.txt", "r") as file:
            api_key = file.read().strip()

        city = request.form.get("query")
        
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,           
            "appid": api_key,    
            "units": "metric"     
        }
        resp = requests.get(base_url, params=params)
        if resp.status_code == 200:
            return render_template("weather.html", weather = resp.json())
        else:
            return render_template("weather.html", error = resp.text)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8000)