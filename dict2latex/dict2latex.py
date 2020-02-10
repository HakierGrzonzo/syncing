import json, os
def inputFile(fileName):
    with open(fileName, 'r') as f:
        dane = json.load(f)
        res = list()
        for k, v in dane.items():
            res.append(v)
    return res

dane = inputFile('../zastpw/teachers.json')
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
