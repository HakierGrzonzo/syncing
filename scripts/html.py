dane = input() + ' '
dane = dane.split('<')
dane = [x.split('>', 1) for x in dane]
res = str()
for x in dane:
    try:
        x[0] = x[0].upper()
        res += "<" + x[0] + '>' + x[1]
    except:
        for y in x:
            res+= y
print(res[:len(res) -1])
