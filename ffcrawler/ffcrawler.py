import AO3, time, json
from pprint import pprint

from AO3.utils import kudos

def pWait(interval):
    for i in range(interval + 1):
        print("\r{}/{}".format(i, interval), end="")
        time.sleep(1)
    print()
        

Show = "The Dragon Prince (Cartoon)"

search = AO3.Search(fandoms=Show, kudos=AO3.utils.Constraint(40))
search.update()
total = search.total_results
print("Found {} works".format(search.total_results))
works = list()
page = 1

skipped = 0
for work in search.results:
    works.append(work)

rateLimitedCount = 0

try:
    while True:
        search.page = page
        try:
            search.update()
            page += 1
        except AO3.utils.HTTPError:
            rateLimitedCount += 1
            timer = rateLimitedCount * 30
            print("\nRatelimit detected! trying again in {} seconds".format(timer))
            pWait(timer)
            continue
        for work in search.results:
            if work not in works:
                works.append(work)
            else:
                skipped += 1
        print("Got {}/{} works".format(len(works), total), end="\r")
        if len(search.results) < 20 or len(works) >= total:
            break
except KeyboardInterrupt:
    print("\nrecived interrupt, proceeding with {} works..".format(len(works)))

print("\nWaiting for RateLimit")
print("Skipped {} works".format(skipped))
pWait(60)
print("Processing works!")
results = list()
cached = list()
try:
    with open("result.json", "r") as f:
        results = json.load(f)
        cached = list([x["url"] for x in results])
        print("Continuing from file")
except Exception as e:
    print(e)


try:
    for workid in works:
        print("\rProcessing work {}/{}".format(len(results) + 1, len(works)), end="")
        if workid.url not in cached:
            this_rate_limit = 3
            id = AO3.utils.workid_from_url(workid.url)
            while True:
                try:
                    work = AO3.Work(id)
                    res = {
                        "title" : work.title,
                        "hits" : work.hits,
                        "kudos" : work.kudos,
                        "language" : work.language,
                        "url" : work.url,
                        "chapters" : work.chapters,
                        "words" : work.words,
                        "rating": work.rating,
                        "categories" : work.categories,
                        "characters" : work.characters,
                        "tags" : work.tags,
                        "date_updated" : work.date_updated.isoformat(),
                        "authors": [
                            {
                                "username" : author.username,
                                "url" : author.url
                            }
                            for author in work.authors
                        ],
                        "relationships" : work.relationships
                    }
                    results.append(res)
                    break
                except AO3.utils.HTTPError as e:
                    this_rate_limit += 1
                    timer = this_rate_limit * 30
                    if this_rate_limit > 5:
                        print("\nSkiping this fic!")
                        rateLimitedCount -= this_rate_limit
                        break
                    print("\nRatelimit detected! trying again in {} seconds".format(timer))
                    pWait(timer)
                    continue
    if len(results) % 100 == 0:
        with open("result.json", "w+") as f:
            f.write(json.dumps(results, indent= 4))
            print("\nWriting results to file")
except KeyboardInterrupt:
    print("\nrecived interrupt, proceeding with {} works..".format(len(results)))


print()
print("writing results!")
with open("result.json", "w+") as f:
    f.write(json.dumps(results, indent= 4))
print("finished")
