import json, datetime, os
import AO3, argparse

def downloadWork(work, lastUpdate = None, forced = False, prefix = ""):
    print("Checking {}".format(work.title))
    if lastUpdate == None or forced or work.date_updated != lastUpdate:
        print("Downloading {}, updated {} days ago.".format(work.title, (datetime.date.today() - work.date_updated).days))
        print(work.summary)
        fname = prefix + (" " if len(prefix) > 0 else "") +  work.title + ".epub"
        print("Downloading as {}...".format(fname))
        work.download_to_file(prefix + work.title, "EPUB")

parser = argparse.ArgumentParser(
    description = "A crude A03 fanfiction checker",prog="GetFanFic.py"
)
parser.add_argument('url', type = str, help = "URLs to add to the list of checked works", metavar="url", nargs='*')
parser.add_argument('-f', dest = "forced", help = "Download all works, even if there were no updates")
args = parser.parse_args()

data = []
try:
    data = json.load(open(os.path.expanduser("~/.fanfic2.json"), "r"))
except:
    pass

series_ids = list()
urls = list()
for point in data:
    url = point.get("url")
    if url is None:
        url = "https://archiveofourown.org/series/{}".format(point.get("id"))
        series_ids.append(point.get("id"))
    urls.append(url)


if args.url is not None:
    for arg in args.url:
        if arg not in urls:
            data.append({"url": arg})
res = []
for item in data:
    try:
        series = None
        isSeries = False
        if "works" in item.get("url", str()):
            work = AO3.Work(AO3.utils.workid_from_url(item["url"]))
            if len(work.series) == 0:
                downloadWork(work, datetime.date.fromisoformat(item.get("update")) if item.get("update") is not None else None, args.forced != None)
                item["update"] = work.date_updated.isoformat()
                res.append(item)
                continue
            else:
                series = work.series[0]
                series.reload()
                if series.seriesid in series_ids:
                    continue
                item["id"] = series.seriesid
                item = {"series": {}, "id" : series.seriesid}
                print("Adding new series {}".format(series.name))
                isSeries = True

        if "series" in item.get("url", str()) or item.get("id") is not None or isSeries:
            if series is None and item.get("series") is None:
                series = AO3.Series(AO3.utils.workid_from_url(item["url"]))
                item = {"series": {}, "id" : series.seriesid}
                print("Adding new series {}".format(series.name))
            elif series is None:
                series = AO3.Series(item["id"])
            i = 0
            for work in series.work_list:
                work.reload()
                series_item = item.get("series", dict()).get(work.url)
                if series_item is None:
                    series_item = dict()
                    print("Adding new member {} to series {}".format(work.title, series.name))
                downloadWork(work, datetime.date.fromisoformat(series_item.get("update")) if series_item.get("update") is not None else None, args.forced != None, "{}_{}".format(series.name, i))
                series_item["update"] = work.date_updated.isoformat()
                item["series"][work.url] = series_item
                i += 1
            res.append(item)
    except Exception as e:
        print(e)
        print(item)
        res.append(item)
        raise e
json.dump(res, open(os.path.expanduser("~/.fanfic2.json"), "w+"), indent = 4)
print("Done!")