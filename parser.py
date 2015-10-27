import feedparser
import datetime

f = feedparser.parse('https://nvd.nist.gov/download/nvd-rss.xml')


class CVE(object):
    """CVE basic object"""
    
    def __init__(self, rss_entry):
        self.date = ""
        self.cveid = ""
        self.parse(rss_entry)

    def parse(self, entry):
        self.date = ""
        try:
            self.date = datetime.datetime.strptime(entry["updated"],"%Y-%m-%dT%H:%M:%SZ")
        except ValueError as e:
            print("invalid date:", e)

        self.cveid = entry["title"].split(" ")[0]


    def __repr__(self):
        return "%s: %s" % (str(self.date), self.cveid)
    
class BDD(object):
    """bdd object that will use SQLalchemy"""

    def __init__(self):
        pass

    def connect(self):
        pass

    def add(self, cve):
        pass

    
if __name__ == "__main__":

    bdd = BDD()
    bdd.connect()
    
    for v in f["entries"]:
        c = CVE(v)
        print(c)
        bdd.add(c)
    
    

