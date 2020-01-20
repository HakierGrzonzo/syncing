from bs4 import BeautifulSoup
import json, requests, os

site = 'http://www.lo1.gliwice.pl/wp-content/uploads/plan'


def getPlan(site):
    # Walk the sidebar to generate list of urls pointing to shedules
    r = requests.get(site + '/lista.html')
    soup = BeautifulSoup(r.content, features = 'lxml')
    links = list()
    for link in soup.find_all('a'):
        # only get links to class shedules, ignore teachers. Class numbers are 3 characters long
        if len(link.text) == 3:
            links.append(link.get('href'))
    # Download shedules and parse the HTML
    plans = dict()
    for link in links:
        r = requests.get(site + '/' + link)
        soup = BeautifulSoup(r.content, features = 'lxml')
        klasa = soup.find('span', {'class':'tytulnapis'}).text.strip()
        soup = soup.find('table', {"class": "tabela"})
        # Parse the table into dict
        headings = [collumn.text for collumn in soup.find_all('th')]
        plan = dict()
        # generate keys for the dict
        for heading in headings:
            plan[heading] = list()
        for row in soup.find_all('tr')[1:]:
            # walk over rows, set up iterator x for headings
            x = 0
            for cell in row.find_all('td'):
                if len(list(cell.descendants)) > 1:
                    string = str()
                    for text in cell.find_all(['span', 'a']):
                        string += text.text + ' '
                    string = string.strip().replace('-', ' ').replace('DW ', '').split(' ')
                    res = list()
                    i = 0
                    last = 0
                    stringIter = string.copy()
                    for z in stringIter:
                        if z[:2].isnumeric():
                            res.append(string[last:i +1])
                            last = i + 1
                        i += 1
                    plan[headings[x]].append(res)
                else:
                    plan[headings[x]].append(cell.text.strip())
                x += 1
        plans[klasa] = plan
    with open('planLekcji.json', 'w+') as f:
        f.write(json.dumps(plans, indent = 4))
    return plans



def main():
    getPlan(site)

if __name__ == '__main__':
    main()
