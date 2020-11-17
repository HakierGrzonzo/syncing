import requests, base64, json
from bs4 import BeautifulSoup as Soup

MAX_PORT = 50000
HOST = "192.168.152.113"

result = list()
portList = [80] + list(range(1000, MAX_PORT + 1))

try:
    for port in portList:
        url = "http://{}:{}/".format(HOST, port)
        try:
            response = requests.get(url)
            res = {
                "url" : response.url,
            }
            try:
                res["title"] = Soup(response.text, features="lxml").find("title").text
            except:
                pass
            try:
                favget = requests.get(url + "favicon.ico")
                res["favicon.ico"] = base64.encodebytes(favget.content).decode("utf-8") if favget.status_code == 200 else None
            except:
                pass
            result.append(res)
        except:
            pass
        if port % 500 == 0:
            print("\r{}/{}".format(port, MAX_PORT), end="")
except KeyboardInterrupt:
    pass

print("\rDone, writing output to json file")
with open("ports.json", "w+") as f:
    json.dump(result, f)
