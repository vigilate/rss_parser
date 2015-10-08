import feedparser

f = feedparser.parse('https://nvd.nist.gov/download/nvd-rss.xml')

for v in f["entries"]:
    print("%s | %s" % (v["updated"], v["title"]))
    print("v" * 50)
    print("%s" % v["summary"])
    print("^" * 50)

