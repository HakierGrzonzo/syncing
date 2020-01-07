from bs4 import BeautifulSoup
import requests, json, os, sys, multiprocessing

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
            print('Managed to get info on:\t' + fanfic['title'] + '\tLast updated:\t' + fanfic['lastUpdate'])
            return json.dumps(fanfic)
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
        print('Downloading: ' + title)
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
    f = open(vaultFile, 'w+')
    f.write(json.dumps(data, indent = 4))
    f.close()

vaultFile = os.path.expanduser('~/.fanfics.json')
site = 'https://archiveofourown.org'

if __name__ == '__main__':
    print('Fanfic Downloader v.0')
    identifiers = list()
    if len(sys.argv) > 1:
        if sys.argv[1] == '-F':
            forced = True
            print('Running in forced download mode')
        else:
            forced = False

    for x in sys.argv[1:]:
        if x.startswith(site + '/works/'):
            x = x.replace(site + '/works/','')
        if x.find('/chapter') != -1:
            x = x[:x.find('/chapter')]
        if not x == '-F':
            identifiers.append(str(x))

    dataAll = GetFanficVault()
    data = dataAll['fanfics']

    #Get fanfics from vault to check
    for fanfic in data:
        try:
            if not fanfic['id'] in identifiers:
                identifiers.append(fanfic['id'])
        except Exception as e:
            pass

    # Get info on fanfic updates, in case of failure remove from list
    fanfics = list()
    """
    for id in identifiers:
        fanfics.append(GetFanficInfo(id))
    """
    p = multiprocessing.Pool(4)
    fanfics = p.map(GetFanficInfo, identifiers)
    p.close()
    # Make a list of fanfics that need downloading and download them
    toDownload = list()
    for fanfic in fanfics:
        try:
            if (not fanfic in data or forced) and fanfic != None:
                toDownload.append(fanfic)
        except:
            pass
    if len(toDownload) > 0:
        print('Downloading ' + str(len(toDownload)) + ' fanfics')
        for fanfic in toDownload:
            f = DownoloadFanfic(fanfic)
            f.close()
    else:
        print('Nothing to Download :(')

    # Update Vault
    for fanfic in data:
        if not fanfic in fanfics:
            fanfics.append(fanfic)
    dataAll['fanfics'] = fanfics
    DumpFanficVault(dataAll)
    print('Done')
