from bs4 import BeautifulSoup
import requests, json, os, sys

isColorful = False
def LOLprint(txt):
    if isColorful:
        os.system("echo \"" + str(txt) + "\" | lolcat -a -d 24")
    else:
        print(txt)

def GetFanficInfo(id):
    global site
    try:
        url = site + '/works/' + id
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features = 'lxml')
        fanfic = dict()
        try:
            try:
                fanfic['lastUpdate'] = soup.find('dd', 'status').string
            except:
                fanfic['lastUpdate'] = soup.find('dd', 'published').string
            fanfic['wordcount'] = soup.find('dd','words').string
            fanfic['title'] = soup.find('h2', 'title heading').string.replace('\n      ','').replace('\n    ','')
            fanfic['id'] = id
            LOLprint('Managed to get info on:\t' + fanfic['title'] + '\tLast updated:\t' + fanfic['lastUpdate'])
            return fanfic
        except:
            print('failed to process ' + id)
            return None
    except requests.exceptions.ConnectionError as e:
        print('failure')
        return None
def DownoloadFanfic(fanfic):
    global site
    title = fanfic['title'].replace('\'','') + '.epub'
    try:
        LOLprint('Downloading: ' + title)
        r = requests.get(site + '/downloads/' + fanfic['id'] + '/' + title)
        try:
            os.remove(title)
        except:
            pass
        f = open(title,'wb+')
        f.write(r.content)
        return f
    except requests.exceptions.ConnectionError as e:
        print('failed to download ' + title)
        print(e)
        return None
def GetFanficVault():
    global vaultFile
    try:
        data = json.load(open(vaultFile, 'r'))
    except:
        f = open(vaultFile, 'w+')
        f.write(json.dumps({'name': 'fanficDwnld v.0', 'fanfics': list()}))
        f.close()
        data = json.load(open(vaultFile, 'r'))
    return data
def DumpFanficVault(data):
    global vaultFile
    try:
        os.remove(vaultFile)
    except:
        pass
    f = open(vaultFile, 'w+')
    f.write(json.dumps(data, indent = 4))
    f.close()

vaultFile = os.path.expanduser('~/.fanfics.json')
site = 'https://archiveofourown.org'


def main(args):
    global isColorful
    Data = GetFanficVault()
    FanficIDs = [x['id'] for x in Data['fanfics']]
    Forced = False

    for x in sys.argv[1:]:
        if x.startswith(site + '/works/'):
            x = x.replace(site + '/works/','')
        if x.find('/chapter') != -1:
            x = x[:x.find('/chapter')]
        if x == '-F':
            LOLprint('Running in forced download mode')
            Forced = True
        elif x == '-c':
            isColorful = True
        else:
            FanficIDs.append(str(x))
    LOLprint('FanficDownloader v.1')
    ToDownload = list()
    fics = list()
    for id in FanficIDs:
        fanfic = GetFanficInfo(id)
        if fanfic != None:
            fics.append(fanfic)
            if fanfic not in Data['fanfics'] or Forced:
                DownoloadFanfic(fanfic)
    Data['fanfics'] = fics
    DumpFanficVault(Data)


if __name__ == '__main__':
    args = sys.argv
    main(args)
