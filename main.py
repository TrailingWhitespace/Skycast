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
            api_key = file.read()

        city = request.form.get("query")
        
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,           
            "appid": api_key,    
            "units": "metric"     
        }
        resp = requests.get(base_url, params=params)
        if resp.status_code == 200:
            print(resp.json())
            return render_template("weather.html")
        else:
            return render_template("weather.html", error = resp.text)




if __name__ == '__main__':
    app.run(debug=True, port = 8000)