import json, os
def inputFile(fileName):
    with open(fileName, 'r') as f:
        dane = f.readlines()
        dane = [x.split(',') for x in dane]
        res = list()
        sample = dict()
        for x in dane[0]:
            x = x.strip()
            sample[x] = None
        for x in dane:
            osoba = sample.copy()
            i = 0
            for k, v in sample.items():
                osoba[k] = x[i]
                i += 1
            res.append(osoba)
    return res

dane = inputFile('dane.csv')
print('got', len(dane), 'people!')
with open('Template.tex', 'r') as f:
    template = f.read()
with open('frameTemplate.tex', 'r') as f:
    frame_raw = '\n' + f.read().strip() + '\n'

res = str()
for osoba in dane:
    frame = frame_raw
    for k, v in osoba.items():
        frame = frame.replace('?'+k, v)
    res += '\n\n' + frame

with open('output.tex', 'w+') as f:
    f.write(template.replace('?marker', res))
print('output wiritten to output.tex, attempting to run LaTeX')
os.system('latex output.tex')
