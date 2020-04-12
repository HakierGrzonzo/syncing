from app import app
from flask import render_template, request

osoby = list()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/gra')
def gra():
    global osoby
    nick = request.args.get('nick')
    if not nick in osoby:
        osoby.append(nick)
    if len(osoby) == 1:
        pierwsza = "1"
        print('pierwsza osoba to: ', nick)
    elif nick == osoby[0]:
        pierwsza = "1"
    else:
        pierwsza = None
    url = '/gra?nick=' + nick
    return render_template('gra.html', url = url, nick = nick, pierwsza = pierwsza, osoby = osoby)

@app.route('/reset')
def reset():
    global osoby
    stareOsoby = osoby.copy()
    osoby = list()
    if len(stareOsoby) == 0:
        stareOsoby.append('Nikt się nie zgłosił :(')
    print('Zresetowano listę')
    return render_template('reset.html', osoby = stareOsoby)
