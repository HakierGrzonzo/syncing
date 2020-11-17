from flask import Flask, render_template
import base64, requests, json
from bs4 import BeautifulSoup as Soup

MAX_PORT = 50000
HOST = "192.168.152.113"

app = Flask(__name__)

services = dict()

def updateServices():
    global services
    result = dict()
    portList = [80] + list(range(1000, MAX_PORT + 1))
    for port in portList:
        url = "http://{}:{}/".format(HOST, port)
        try:
            response = requests.get(url)
            res = {
                "url": response.url
            }
            try:
                res["title"] = Soup(response.text, features="lxml").find("title").text
            except:
                pass
            result[port] = res
        except:
            pass
    print("Found {} services".format(len(result)))
    services = result.copy()
    with open("ports.json", "w+") as f:
        json.dump(result, f)

try:
    with open("ports.json", "r") as f:
        services = json.load(f)
except:
    updateServices()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", services = services)

@app.route("/update")
def update():
    updateServices()
    return "Update Done"

if __name__ == "__main__":
    app.run(debug = True)