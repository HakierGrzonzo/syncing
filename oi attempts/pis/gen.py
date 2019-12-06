
def repeats(words):
    res = dict()
    for word in words:
        try:
            res[word] += 1
        except:
            res[word] = 1
    return res

def handleText(text, num = 500):
    text = text.split(" ")
    count = len(text)
    print("ok")
    res = repeats(text)
    for k, v in res.items():
        if v > num and len(k) > 1:
            print(k + "\t" + str(int(v/count*1000)))


if __name__ == "__main__":
    directory = "pis_dlazaw/"
    files = ["Prus.txt", "Sienkiewicz.txt", "Mickiewicz.txt"]
    texts = list()
    for x in files:
        texts.append(open(directory + x, "r").read().lower().replace("a", "").replace("e", "").replace("o")

    print(texts[2])
