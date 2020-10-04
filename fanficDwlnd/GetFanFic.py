from bs4 import BeautifulSoup
import requests, json, os, sys, datetime, time

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux 5.6.15-1-MANJARO x86_64) KHTML/5.70.0 (like Gecko) Konqueror/5 KIO/5.70'}
cookie = {'view_adult': "true"}

isColorful = False
def LOLprint(txt):
    if isColorful:
        os.system("echo \"" + str(txt) + "\" | lolcat -a -d 24")
    else:
        print(txt)

def PrintTimeDelta(dateString):
    y, m, d = [int(x) for x in dateString.split('-')]
    date = datetime.date(y, m, d)
    return str((datetime.date.today() - date).days)
def GetFanficInfo(id):
    global site
    try:
        url = site + '/works/' + id
        r = requests.get(url, headers = headers, cookies = cookie)
        if r.status_code == 500:
            print('Error 500, is the server overloaded? retrying in 10 seconds.')
            time.sleep(10)
            r = requests.get(url, headers = headers, cookies = cookie)
        if r.status_code != 200:
            print('Error on {}: {}'.format(id, r.status_code))
            raise Exception('http error')
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
            for link in soup.find('ul', 'expandable secondary').find_all('a'):
                if link.text.strip() == 'EPUB':
                    fanfic['link'] = site + link.get('href')
                    break
            fanfic['status'] = True
            LOLprint('Managed to get info on:\t' + fanfic['title'] + '\tLast updated ' + PrintTimeDelta(fanfic['lastUpdate']) + ' days ago')
            return fanfic
        except requests.exceptions.ReadTimeout:
            print('failed to process ' + id)
            return {'status': False, 'id' : id}
        except Exception as e:
            print('failed to process {}: {}'.format(id, r.status_code))
            return {'status': False, 'id' : id}
    except Exception as e:
        print('failure', e)
        return {'status': False, 'id' : id}

def DownoloadFanfic(fanfic):
    global site
    title = fanfic['title'].replace('\'','') + '.epub'
    try:
        LOLprint('Downloading: ' + title)
        r = requests.get(fanfic['link'], headers = headers, cookies = cookie)
        try:
            os.remove(title)
        except:
            pass
        f = open(title,'wb+')
        f.write(r.content)
        f.close()
        return True
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
            if (fanfic not in Data['fanfics'] or Forced) and fanfic['status']:
                DownoloadFanfic(fanfic)
    Data['fanfics'] = fics
    DumpFanficVault(Data)


if __name__ == '__main__':
    args = sys.argv
    main(args)
