from bs4 import BeautifulSoup as bs
import requests, json, os

site = 'http://www.lo1.gliwice.pl/zastepstwa-2/'

def GetZast(site):
    r = requests.get(site)
    print('done')
    soup = bs(r.content, features='lxml')
    return soup.find('div','page post-3833 type-page status-publish hentry')

class Zastempstwa(object):
    def __init__(self, _raw):
        super(Zastempstwa, self).__init__()
        self.raw = _raw
        self.lines = list()
        for x in self.raw.find_all('p'):
            if (not x.text.isspace()) and x.text != None:
                self.lines.append(x.text.replace('\n','').strip())
        self.ParseLines()
    def ParseLines(self):
        def isLesson(str):
            for x in str:
                if x.isnumeric() or x == ',' or x == ' ':
                    pass
                elif x == 'l':
                    return True
                else:
                    return False
        self.zastepstwa = list()
        for line in self.lines:
            if line.startswith('Zastępstwa'):
                self.date = line[len('Zastępstwa'):].strip().split('.')
            elif isLesson(line):
                self.zastepstwa.append(line)



def main():
    with open('dane.txt', 'r') as f:
        soup = bs(f.read(), features='lxml')
        zastepstwa = Zastempstwa(soup.find('div','page post-3833 type-page status-publish hentry'))
    print(zastepstwa.lines)

if __name__ == '__main__':
    main()
