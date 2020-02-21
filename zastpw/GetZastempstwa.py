from bs4 import BeautifulSoup as bs
import requests, json, os
from fuzzyfinder import fuzzyfinder

site = 'http://www.lo1.gliwice.pl/zastepstwa-2/'

def GetZast(site):
    r = requests.get(site)
    print('done')
    soup = bs(r.content, features='lxml')
    return soup.find('div','page post-3833 type-page status-publish hentry')

def parseTeacherList(fname):
    with open(fname, 'r') as source:
        with open('teachers.json', 'w+') as destination:
            lines = source.readlines()
            teachers = dict()
            for line in lines:
                parms = line.split(' ')
                teacher = dict()
                teacher['name'] = parms[0]
                teacher['surname'] = parms[1]
                teachers[parms[2].replace('[', '').replace(']','').replace('\n','')] = teacher
            destination.write(json.dumps(teachers, indent = 4))


class Zastempstwa(object):
    def __init__(self, _raw = None, teacherFile = 'teachers.json', sheduleFile = 'planLekcji.json'):
        super(Zastempstwa, self).__init__()
        if _raw != None:
            self.raw = _raw
        else:
            self.raw = GetZast(site)
        self.lines = list()
        for x in self.raw.find_all('p'):
            if (not x.text.isspace()) and x.text != None:
                self.lines.append(x.text.replace('\n','').strip())
        with open(teacherFile, 'r') as f:
            self.teachers = json.loads(f.read())
        with open(sheduleFile, 'r') as f:
            self.plan = json.loads(f.read())
        self.ParseLines()
    def findTeacherID(self, string):
        result = str()
        surnameList = [x['surname'] for k, x in self.teachers.items()]
        surname = string
        while len(surname) > 2:
            res = list(fuzzyfinder(surname, surnameList))
            if len(res) == 0:
                surname = surname[:len(surname) - 1]
            else:
                surname = res[0]
                break
        if surname in surnameList:
            for id, teacher in self.teachers.items():
                if surname == teacher['surname']:
                    return id
        else:
            return str()
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
        surnameList = [x['surname'] for k, x in self.teachers.items()]
        for line in self.lines:
            if line.startswith('Zastępstwa'):
                self.date = line[len('Zastępstwa'):].strip().split('.')
            elif isLesson(line):
                self.zastepstwa.append(line)
            elif not(line.find('matur') != -1 or line.find('międzynarodo') != -1):
                string = line.strip().split(' ')
                self.absences = list()
                for x in string:
                    if len(x) > 3:
                        teacher = self.findTeacherID(x)
                        if not teacher == None:
                            self.absences.append(teacher)
    def ParseZastempstwa(self):
        def romanize(klasa):
            """change the class number to Zastępstwa format"""
            if klasa[len(klasa) - 1] == 'L':
                # Strip L form the end of string
                klasa = klasa[:len(klasa) - 1]
            if klasa[0] == '1':
                return str('I' + klasa[1].upper() + klasa[2:])
            elif klasa[0] == '2':
                return str('II' + klasa[1].upper() + klasa[2:])
            elif klasa[0] == '3':
                return str('III' + klasa[1].upper() + klasa[2:])
            elif klasa[0] == '4':
                # Compatibility with education reform
                return str('IV' + klasa[1].upper() + klasa[2:])
            else:
                return klasa
        klasy = [romanize(k) for k, v in self.plan.items()]
        lines = self.zastepstwa.copy()
        res = list()
        for line in lines:
            line = line.split(' ')
            zastempstwo = dict()
            # zastempstwo['raw'] = line
            zastempstwo['godziny'] = line[0].replace('l', '').split(',')
            if line[2] not in klasy:
                pre = str()
                post = str()
                classes = list()
                for char in line[2]:
                    if char == 'I':
                        pre += char
                    elif char == char.upper():
                        classes.append(char)
                    else:
                        post += char
                classes = [str(pre + x + post) for x in classes]
                for x in classes:
                    assert x in klasy
                zastempstwo['klasa'] = classes
            else:
                zastempstwo['klasa'] = line[2]
            # Handle groups
            lastTeacher = 3
            if 'gr.' == line[3]:
                AbsentTeacher = list()
                expectingTeacher = True
                for text in line[4:]:
                    if text != 'p.' and expectingTeacher:
                        code = self.findTeacherID(text)
                        expectingTeacher = False
                        AbsentTeacher.append(code)
                        lastTeacher = line.index(text) + 1
                    elif text == 'i':
                        expectingTeacher = True
                    elif text != 'p.':
                        break
                zastempstwo['group'] = AbsentTeacher
            else:
                zastempstwo['group'] = 'all'
            if 'zwolniona' in line and 'do' in line and 'domu' in line:
                zastempstwo['substitution'] = 'zwolniona'
            elif 'przychodzi' in line and 'na' in line:
                zastempstwo['substitution'] = 'zwolniona'
            else:
                text = str()
                for x in line[lastTeacher:]:
                    text += x +' '
                zastempstwo['substitution'] = text.strip()
            res.append(zastempstwo)
        self.parsedZastempstwa = res
        return res

def main():
    parseTeacherList('teachers.txt')
    zastempstwa = Zastempstwa()
    print(zastempstwa.lines)
    while True:
        klasa = input('klasa: ')
        for x in zastempstwa.ParseZastempstwa():
            if x['klasa'] == klasa:
                print(json.dumps(x, indent = 4))

if __name__ == '__main__':
    main()
